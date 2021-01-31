import sys
test = int(sys.stdin.readline().strip())
for _ in range(test):
    r, n = map(int, sys.stdin.readline().split())
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)]

    for i in range(n+1):
        cache[i][0]=1
    for i in range(r+1):
        cache[i][i]=1
    for i in range(1, n+1):
        for j in range(1, r+1):
            cache[i][j]= cache[i-1][j-1]+ cache[i-1][j]

    print(cache[n][r])