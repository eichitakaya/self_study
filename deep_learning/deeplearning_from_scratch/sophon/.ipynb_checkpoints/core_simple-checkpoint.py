import weakref

import numpy as np

#各種関数

class Config:
    enable_backprop = True

    import numpy as np
# pytorchのtensorに対応？
class Variable:
    __array_priority__ = 200
    
    def __init__(self, data, name=None):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{} is not supported!'.format(type(data)))
                
        self.data = data
        self.name = name # 名前を付ける機能．計算グラフ等を可視化するときに便利
        self.grad = None
        self.creator = None
        self.generation = 0
    
    def set_creator(self, func):
        self.creator = func
        self.generation = func.generation + 1
    
    def backward(self, retain_grad=False): # 再帰ではなくループで実装
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        
        funcs = []
        seen_set = set() # 同じ関数が重複しないようにする
        
        def add_func(f):
            if f not in seen_set:
                funcs.append(f)
                seen_set.add(f)
                funcs.sort(key=lambda x: x.generation) # この部分は，優先度付きキューを用いて効率化できるらしい．
        
        add_func(self.creator)
        
        while funcs:
            f = funcs.pop() # 自身を生み出した関数を取得
            gys = [output().grad for output in f.outputs] # 弱参照のため output()となっている．
            gxs = f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)
                
            for x, gx in zip(f.inputs, gxs):
                if x.grad is None:
                    x.grad = gx
                else: # 同じ変数が入力された場合
                    x.grad = x.grad + gx
                    
                if x.creator is not None:
                    add_func(x.creator) # 1つ前の関数をリストに追加
            
            if not retain_grad:
                for y in f.outputs:
                    y().grad = None # 弱参照なので y()
    
    def clearglad(self):
        self.grad = None
    
    @property
    def shape(self): # @propertyをつけると，x.shapeのように()を付けずに発動できる
        return self.data.shape
    
    @property
    def ndim(self):
        return self.data.ndim
    
    @property
    def size(self):
        return self.data.size
    
    @property
    def dtype(self):
        return self.data.dtype
    
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        if self.data is None:
            return 'variable(None)'
        p = str(self.data).replace('\n', '\n' + ' ' * 9)
        return 'variable(' + p + ')'
    
def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x

def as_variable(obj):
    if isinstance(obj, Variable):
        return obj
    return Variable(obj)

class Function:
    def __call__(self, *inputs): # アスタリスクにより，複数入力に対応
        inputs = [as_variable(x) for x in inputs]
        
        xs = [x.data for x in inputs] # 複数入力に対応
        ys = self.forward(*xs) # 複数入力（アスタリスクを付けてアンパッキング）に応じた複数出力
        if not isinstance(ys, tuple): # タプルでない場合は無理やりタプルに変換
            ys = (ys, )
        outputs = [Variable(as_array(y)) for y in ys]
        
        if Config.enable_backprop:
            self.generation = max([x.generation for x in inputs])
            for output in outputs:
                output.set_creator(self) # 出力変数に生成元の関数を覚えさせる
            self.inputs = inputs # 入力された変数を覚えておく
            self.outputs = [weakref.ref(output) for output in outputs] # 出力も覚えておく，weakrefを使うことによりメモリ管理を効率化
        
        # リストの要素が1つのときは最初の要素を返す
        return outputs if len(outputs) > 1 else outputs[0]
    
    def forward(self, xs):
        raise NotImplementedError()
    
    def backward(self, gys):
        raise NotImplementedError()

        
# 足し算
class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return y
    
    def backward(self, gy):
        return gy, gy
    
def add (x0, x1):
    x1 = as_array(x1)
    return Add()(x0, x1)


# 負数
class Neg(Function):
    def forward(self, x):
        return -x
    
    def backward(self, gy):
        return -gy

def neg(x):
    return Neg()(x)


# 引き算
class Sub(Function):
    def forward(self, x0, x1):
        y = x0 - x1
        return y
    
    def backward(self, gy):
        return gy, -gy
    
def sub(x0, x1):
    x1 = as_array(x1)
    return Sub()(x0, x1)

def rsub(x0, x1):
    x1 = as_array(x1)
    return Sub()(x1, x0) # x1, x0を入れ替え


# 掛け算
class Mul(Function):
    def forward(self, x0, x1):
        y = x0 * x1
        return y
    
    def backward(self, gy):
        x0, x1 = self.inputs[0].data, self.inputs[1].data
        return gy * x1, gy * x0

def mul(x0, x1):
    x1 = as_array(x1)
    return Mul()(x0, x1)


# 割り算
class Div(Function):
    def forward(self, x0, x1):
        y = x0 / x1
        return y
    
    def backward(self, gy):
        x0, x1 = self.inputs[0].data, self.inputs[1].data
        gx0 = gy / x1
        gx1 = gy * (-x0 / x1 ** 2)
        return gx0, gx1

def div(x0, x1):
    x1 = as_array(x1)
    return Div()(x0, x1)

def rdiv(x0, x1):
    x1 = as_array(x1)
    return Div(x1, x0) # x1, x0を入れ替え


# 累乗
class Pow(Function):
    def __init__(self, c):
        self.c = c
        
    def forward(self, x):
        y = x ** self.c
        return y
    
    def backward(self, gy):
        x = self.inputs[0].data
        c = self.c
        gx = c * x ** (c - 1) * gy
        return gx
    
def pow(x, c):
    return Pow(c)(x)


# with構文でenable_backpropをFalseにするための準備
import contextlib

@contextlib.contextmanager
def using_config(name, value):
    old_value = getattr(Config, name)
    setattr(Config, name, value)
    try:
        yield
    finally:
        setattr(Config, name, old_value)

def no_grad():
    return using_config('enable_backprop', False)


def setup_variable():
    Variable.__add__ = add
    Variable.__radd__ = add
    Variable.__mul__ = mul
    Variable.__rmul__ = mul
    Variable.__neg__ = neg
    Variable.__sub__ = sub
    Variable.__rsub__ = rsub
    Variable.__truediv__ = div
    Variable.__rtruediv__ = rdiv
    Variable.__pow__ = pow