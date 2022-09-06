import argparse
try:
    import matplotlib
    matplotlib.use('Agg')
except ImportError:
    pass
import chainer
import chainer.functions as F
import chainer.links as L
from chainer import training
from chainer.training import extensions

class Autoencoder(chainer.Chain):
    def __init__(self):
        super(Autoencoder, self).__init__(
                encoder = L.Linear(784, 64),
                decoder = L.Linear(64, 784))

    def __call__(self, x, hidden=False):
        h = F.relu(self.encoder(x))
        if hidden:
            return h
        else:
            return F.relu(self.decoder(h))

# MNISTのデータの読み込み
train, test = chainer.datasets.get_mnist()

# 教師データ
train = train[0:1000]
train = [i[0] for i in train]
train = tuple_dataset.TupleDataset(train, train)
train_iter = chainer.iterators.SerialIterator(train, 100)

# テスト用データ
test = test[0:25]
