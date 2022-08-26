import numpy as np

HW_1 = input().split()
H_1 = int(HW_1[0])
W_1 = int(HW_1[1])
A = []
for i in range(H_1):
    A.append(input().split())
A = np.array(A)

HW_2 = input().split()
H_2 = int(HW_2[0])
W_2 = int(HW_2[1])
B_arr = []
B_set = []
for i in range(H_2):
    tmp = input().split()
    B_arr.append(tmp)
    for j in range(W_2):
        B_set.append(tmp[i])

B_arr = np.array(B_arr)
B_set = list(set(B_set))

# Bの要素が含まれない場合，Aの行を削除
for i in range(H_1):
    flag = 0
    for j in range(len(B_set)):
        if B_set[j] in A[i]:
            flag = 1
        else:
            continue
    if flag == 0:
        A = np.delete(A, i, 0)
