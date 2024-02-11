# A_i = A_j になる組を数えて，全体の組数から引けばよい

from collections import defaultdict

N = int(input())
A = input().split(" ")


exist = defaultdict(int)
all = N * (N - 1) / 2
swappable_cnt = 0

for i in range(N):
    exist[A[i]] += 1

for i in exist:
    if exist[i] != 1:
        swappable_cnt += exist[i] * (exist[i] - 1) / 2

result = all - swappable_cnt
print(int(result))
