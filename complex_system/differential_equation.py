# Mayモデル
def func(x, t, r, K, c, h, H):
    dxdt = r * x * (1 - x / K) - c * x ** 2 / (h ** 2 + x ** 2)
    return dxdt