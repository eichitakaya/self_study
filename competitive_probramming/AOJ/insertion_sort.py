N = int(input())

A = []

nums = input().split()

for i in range(N):
    A.append(int(nums[i]))

l = [str(i) for i in A]
print(" ".join(l))
    
for i in range(1, N):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = v
    l = [str(i) for i in A]
    print(" ".join(l))
