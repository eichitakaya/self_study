# モンテカルロ法で円周率を計算する

import random
import math

def calculate_pi(n):
    num_point_circle = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            num_point_circle += 1
    return 4 * num_point_circle / n

if __name__ == '__main__':
    print(calculate_pi(10000000))