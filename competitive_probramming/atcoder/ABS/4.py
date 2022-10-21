N = int(input())
As = list(map(int, input().split()))

cnt = 0
flag = 0


while flag == 0:

    swap = []
    for a in As:
        if a % 2 != 0:
            flag = 1
            break
        else:
            swap.append(a/2)
    As = swap
    if flag == 0:
        cnt += 1

print(cnt)