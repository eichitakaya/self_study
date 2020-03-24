"""
N = int(input())

maxv = -1 * 10**9
Rs = [int(input())]

for i in range(1, N):
    Rs.append(int(input()))
    for j in range(i):
        maxv = max(maxv, Rs[i] - Rs[j])

print(maxv)
"""

N = int(input())

maxv = -1 * 10 ** 9

minv = int(input())

for i in range(N-1):
    R = int(input())
    maxv = max(maxv, R - minv)
    minv = min(minv, R)

print(maxv)