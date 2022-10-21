S = input()
T = input()

if len(S) > len(T):
    print("No")
else:
    flag = 0
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            flag = 1
    
    if flag == 0:
        print("Yes")
    else:
        print("No")