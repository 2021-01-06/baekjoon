# 에라토스테네스의 채
N, K = map(int, input().split())

check = [False, False] + [True] * (N-1)

eNum = 0
result = 0
for i in range(2, N+1):
    if check[i] == True:
        for j in range(i, N+1, i):
            if check[j] == True:
                check[j] = False
                eNum += 1
                if eNum == K:
                    result = j
    else:
        pass
print(result)
