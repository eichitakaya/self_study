N, M, T = map(int, input().split())

As = list(map(int, input().split())) # i番目の部屋における持ち時間の消費数
XY = {}

flag = 0

for i in range(M):
    X, Y = map(int, input().split())
    XY[X] = Y
#print(XY)
for i in range(N-1):

    T -= As[i]
    if T <= 0:
        print("No")
        flag = 1

    if (i+2) in XY.keys():
        T += XY[i+2] 
    #print(T)
if flag == 0:
    print("Yes")