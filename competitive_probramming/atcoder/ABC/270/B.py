X, Y, Z = map(int, input().split())

if X < 0: # 原点より左にゴール
    if Y > 0: # 原点より右に壁
        print(abs(X))
    elif X < Y < 0: # 原点より左かつ，ゴールより右に壁
        if Y < Z < 0: # 壁と原点の間にハンマー
            print(abs(X))
        elif Z > 0:# 原点より右にハンマー
            print(abs(Z)*2 + abs(X))
        else:
            print(-1)
    else: # ゴールより左に壁
        print(abs(X))
else: # 原点より右にゴール
    if Y < 0: # 原点より左に壁
        print(abs(X))
    elif 0 < Y < X: # 原点より右かつ，ゴールより左に壁
        if 0 < Z < Y: # 壁と原点の間にハンマー
            print(abs(X))
        elif Z < 0: # 原点より左にハンマー
            print(abs(Z)*2 + abs(X))
        else:
            print(-1)
    else: # ゴールより右に壁
        print(abs(X))