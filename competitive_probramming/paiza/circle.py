import math

r = float(input())

r_ceil = math.ceil(r)

cnt = 0
for i in range(r_ceil):
    for j in range(r_ceil):
        if r >= math.sqrt(i**2 + j**2):
            cnt += 1

print(cnt*4)