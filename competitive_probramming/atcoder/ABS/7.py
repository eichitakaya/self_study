alice = 0
bob = 0

N = int(input())

a_list = list(map(int, input().split()))

a_list = sorted(a_list)

for i in range(N):
    if (i+1) % 2 == 0:
        bob += a_list[-(i+1)]
    else:
        alice += a_list[-(i+1)]

print(alice - bob) 