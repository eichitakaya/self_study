import numpy as np
np.random.seed(100)
import cupy as cp
cp.random.seed(100)
import chainer
import chainer.functions as F
import chainer.links as L
from chainer.links import caffe
from chainer import link, Chain, optimizers, Variable

class NormalCNN(chainer.Chain):
    
    def __init__(self, n_out):
        super(NormalCNN, self).__init__()
        with self.init_scope():
            self.conv1 = L.Convolution2D(None, 32, 3, 3, 1)
            self.conv2 = L.Convolution2D(32, 64, 3, 3, 1)
            self.conv3 = L.Convolution2D(64, 128, 3, 3, 1)
            self.fc4 = L.Linear(None, 1000)
            self.fc5 = L.Linear(1000, n_out)
    
    def __call__(self, x):
        h = F.relu(self.conv1(x))
        h = F.relu(self.conv2(h))
        h = F.relu(self.conv3(h))
        h = F.relu(self.fc4(h))
        h = self.fc5(h)
        return h

#----------------------------------------------------------------------------------------------------------------

class ConvBlock(chainer.Chain):
    
    def __init__(self, n_ch, pool_drop=False):
        w = chainer.initializers.HeNormal()
        super(ConvBlock, self).__init__()
        with self.init_scope():
            self.conv = L.Convolution2D(None, n_ch, 3, 1, 1, nobias=True, initialW=w)
            self.bn = L.BatchNormalization(n_ch)
        self.train = True
        self.pool_drop = pool_drop
        
    def __call__(self, x):
        h = F.relu(self.bn(self.conv(x)))
        if self.pool_drop:
            h = F.max_pooling_2d(h, 2, 2)
            h = F.dropout(h, ratio=0.25)
        return h
    
class LinearBlock(chainer.Chain):
    
    def __init__(self):
        w = chainer.initializers.HeNormal()
        super(LinearBlock, self).__init__()
        with self.init_scope():
            self.fc = L.Linear(None, 1024, initialW=w)
        self.train = True
        
    def __call__(self, x):
        return F.dropout(F.relu(self.fc(x)), ratio=0.5)
    
class DeepCNN(chainer.ChainList):

    def __init__(self, n_output):
        super(DeepCNN, self).__init__(
            ConvBlock(64),
            ConvBlock(64, True),
            ConvBlock(128),
            ConvBlock(128, True),
            ConvBlock(256),
            ConvBlock(256),
            ConvBlock(256),
            ConvBlock(256, True),
            LinearBlock(),
            LinearBlock(),
            L.Linear(None, n_output)
        )
        self._train = True

    @property
    def train(self):
        return self._train

    @train.setter
    def train(self, val):
        self._train = val
        for c in self.children():
            c.train = val

    def __call__(self, x):
        for f in self.children():
            x = f(x)
        return x
