# 잔돈을 그르디하게 걸러주기


c = 1000 - int(input())
cs = [500, 100, 50, 10, 5, 1]
cnt = 0
i = 0
# 잔돈이 0 될때까지 리스트를 앞에서부터 돌면서 갯수를 늘려나간다
while c:
    cnt += c // cs[i]
    c -= cs[i] * (c // cs[i])
    i += 1

print(cnt)