X, Y, N = map(int, input().split())

if Y / 3 > X:
    print(X * N)

else:
    print(int(N / 3) * Y + ((N % 3) * X))