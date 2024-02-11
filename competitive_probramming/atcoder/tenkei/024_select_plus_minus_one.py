N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [abs(a - b) for (a, b) in zip(A, B)]

s = sum(diff)

if K >= s and (K - s)%2 == 0:
    print("Yes")
else:
    print("No")