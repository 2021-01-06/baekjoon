# 눈팅후
# dp를 이용한 결국 거의 다 봐야하네
# 후보들은 제곱수들
# 317 ** 2 > 100000
# dp 에는 i에 해당하는 최소 갯수
n = int(input())
dp = [0] * (n+1)
# sq 제곱수들 모아놈 100000 보다 작은
sq = [i ** 2 for i in range(1, 317)]
# dp를 채우자

for i in range(1, n+1):
    s = []
    for j in sq:
        if j > i:
            break
        s.append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[n])

# 후보는 제곱수들