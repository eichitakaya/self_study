import numpy as np
import pandas as pd
from sklearn.datasets import load_wine

class DecisionTree:
    def __init__(self, X, y, gain="gini"):
        self.X = X
        self.y = y
        self.gain = gain

        if gain == "entropy":
            self.info_func = self.comp_entropy
        elif gain == "gini":
            self.info_func = self.gini
    
    def comp_entropy(self, y):
        # 各クラスy_iについて，その発生確率を計算
        probs = [np.sum(y==i)/len(y) for i in np.unique(y)]
        return -np.sum(probs*np.log2(probs))
    
    def comp_gini(self, y):
        probs = [np.sum(y==i)/len(y) for i in np.unique(y)]
        return 1 - np.sum(np.square(probs))

    def select(self, X, y):
        # y全体についてのエントロピーまたは不純度
        all_info = self.info_func(y)

        # 各説明変数を限定した際のエントロピーまたは不純度（メモ用）
        col_infos = []
        gains = []

        for col in X.columns:
            col_info = np.sum([])


if __name__ == '__main__':
    data = load_wine()
    X = data.data
    y = data.target
    t = [1,1,1,1,1,0,0,0,0,0]
    model = DecisionTree(X, t)
    print(model.comp_gini(model.y))
    print(model.y)