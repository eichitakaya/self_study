N = int(input())

A = []

nums = input().split()

for i in range(N):
    A.append(int(nums[i]))

    

flag = 1
a = 0
cnt = 0

while flag:
    flag = 0
    for i in reversed(range(a+1, N)):
        if A[i] < A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
            cnt += 1
            flag = 1
    a += 1

l = [str(i) for i in A]
print(" ".join(l))
print(cnt)