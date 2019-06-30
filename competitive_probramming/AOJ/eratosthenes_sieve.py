import math

def isprime(x):
    if x == 2:
        return True
    
    if x < 2 or x % 2 == 0:
        return False
    
    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2
    
    return True

cnt = 0

n = int(input())

for i in range(n):
    x = int(input())
    if isprime(x) == True:
        cnt += 1
print(cnt)