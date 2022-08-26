H, W = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(H)]

row_sum_list = [sum(row) for row in mat]
col_sum_list = [sum(col) for col in zip(*mat)]


for i in range(H):
    row = []
    for j in range(W):
        row.append(row_sum_list[i] + col_sum_list[j] - mat[i][j])
    print(*row)
