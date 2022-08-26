import numpy as np

H, W = map(int, input().split())

matrix = []
memo = np.zeros((H, W))

for i in range(H):
    row = input()
    matrix.append(row)

i = 0
j = 0
memo[i][j] = 1
for cnt in range(250001):
    #now = [i, j]
    if matrix[i][j] == "U" and i != 0:
        i -= 1
    elif matrix[i][j] == "D" and i != H-1:
        i += 1
    elif matrix[i][j] == "L" and j != 0:
        j -= 1
    elif matrix[i][j] == "R" and j != W-1:
        j += 1
    else:
        print(i+1, j+1)
        break

    if memo[i][j] == 0:
        memo[i][j] = 1
    else:
        print(-1)
        break

