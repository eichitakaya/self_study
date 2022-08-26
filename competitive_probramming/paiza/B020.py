n = int(input())

querys = []
queue = []
current = 0

for i in range(n):
    querys.append(input())

for i in range(n):
    if querys[i] == "go to blank page":
        page = "blank page"
        queue.append(page)
        current += 1
    elif querys[i] == "use the back button":
        current -= 1
        del queue[-1]
        page = queue[current-1]
    else:
        url = querys[i].split()
        url = " ".join(url[2:len(url)])
        page = url
        queue.append(page)
        current += 1
    print(page)
    #print(queue)
    #print(current)

    