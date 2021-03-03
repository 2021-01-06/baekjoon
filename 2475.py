# 검증수 출력
n = list(map(int, input().split()))
for i in range(len(n)):
    n[i] = n[i] ** 2
print(sum(n) % 10)