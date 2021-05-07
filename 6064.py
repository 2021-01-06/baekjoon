# 카잉달력

test_num = 1
M, N, x, y = map(int, input().split())

for i in range(100):
    if i % M == x and i % N == y:
        print(i)
        break
else:
    print(-1)