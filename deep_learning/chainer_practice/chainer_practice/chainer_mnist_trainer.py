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

parser = argparse.ArgumentParser(description='Chainer example: MNIST')
parser.add_argument('--gpu', '-g', type=int, default=-1,
                        help='GPU ID (negative value indicates CPU)')
args = parser.parse_args()

class MnistModel(chainer.Chain):
    def __init__(self):
        super(MnistModel, self).__init__(
                l1 = L.Linear(784, 100),
                l2 = L.Linear(100, 100),
                l3 = L.Linear(100, 10))

    def __call__(self, x):
        h = F.relu(self.l1(x))
        h = F.relu(self.l2(h))
        return self.l3(h)

model = L.Classifier(MnistModel())
if args.gpu >= 0:
        chainer.cuda.get_device(args.gpu).use()  # Make a specified GPU current
        model.to_gpu()  # Copy the model to the GPU
optimizer = chainer.optimizers.Adam()
optimizer.setup(model)

train, test = chainer.datasets.get_mnist()
train_iter = chainer.iterators.SerialIterator(train, 100)
test_iter = chainer.iterators.SerialIterator(test, 100, repeat=False, shuffle=False)

updater = training.StandardUpdater(train_iter, optimizer, device=args.gpu)
trainer = training.Trainer(updater, (3, "epoch"), out="result")
trainer.extend(extensions.Evaluator(test_iter, model, device=args.gpu))
trainer.extend(extensions.LogReport())
trainer.extend(extensions.PrintReport( ["epoch", "main/loss", "validation/main/loss", "main/accuracy", "validation/main/accuracy"]))
trainer.extend(extensions.ProgressBar())

trainer.run()
