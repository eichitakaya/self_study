N = int(input())

sum_list1 = []
sum_list2 = []

sum1 = 0
sum2 = 0

for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        sum1 += P
        sum_list1.append(sum1)
        sum_list2.append(sum2)
    else:
        sum2 += P
        sum_list2.append(sum2)
        sum_list1.append(sum1)

Q = int(input())

result = []
for i in range(Q):
    L, R = map(int, input().split())
    #3, 5の場合，sum_list[4]からsum_list[2]を引けばよい
    if L > 1:
        result1 = sum_list1[R-1] - sum_list1[L-2]
        result2 = sum_list2[R-1] - sum_list2[L-2]
    else:
        result1 = sum_list1[R-1]
        result2 = sum_list2[R-1]
    print(result1, result2)