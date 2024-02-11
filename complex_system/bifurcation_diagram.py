# 分岐図を作成する
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Mayモデル
def func(x, t, r, K, c, h, H):
    dxdt = r * x * (1 - x / K) - c * x ** 2 / (h ** 2 + x ** 2)
    return dxdt

# 微分方程式を解く関数
def solve_ode(func, x0, t, args):
    y = odeint(func, x0, t, args)
    return y


# 初期値
K = 1.0
#c = 0.01
h = 1.0
H = 0.1
r0 = 1.0

r = r0 - H * np.random.rand(1)

t = np.arange(0, 500, 0.01)

# cを変化させて分岐図を作成する
for c in np.arange(0.01, 1.0, 0.01):
    y = solve_ode(func, 0.1, t, args=(r, K, c, h, H))
    plt.plot(c, y[-1], 'k.', markersize=1)
# 図を保存する
plt.savefig('bifurcation_diagram.png')