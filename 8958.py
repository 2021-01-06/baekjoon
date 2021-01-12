n = int(input())

for i in range(n):
    qz = input()
    scr = 0
    cnt = 0
    for j in range(len(qz)):
        if qz[j] == "O":
            cnt += 1
            scr += cnt
        elif qz[j] == "X":
            scr += 0
            cnt = 0
    print(scr)