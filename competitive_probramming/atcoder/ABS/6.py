N, A, B = map(int, input().split())

result = 0

for i in range(N+1):
    s_sum = 0
    for s in str(i):
        s_sum += int(s)
    if A <= s_sum <= B:
        result += i

print(result)
            