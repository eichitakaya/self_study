"""
N個のメモをリストに格納
[0, 0, 0,..., 0] で初期化
入力行におけるi番目の数字がM以上であれば，i番目の要素に1を代入

"""

N, M = map(int, input().split())

memo = []
for i in range(N):
    memo.append(0)

for i in range(N):
    rs = input().split()
    for j in range(N):
        if int(rs[j]) >= M:
            memo[j] = 1

result = []
for i in range(N):
    if memo[i] == 0:
        result.append(i+1)

if len(result) == 0:
    print("wait")
else:
    print(*result)
