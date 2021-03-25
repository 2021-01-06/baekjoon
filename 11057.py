# 다이나믹 프로그램
# N은 자릿수 오름차순의 수를구한다
N = int(input())
dp = [[0 for i in range(10)] for j in range(1001)]
for i in range(10):
    dp[1][i] = 1
for i in range(2, 1001):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i-1][k]
print(sum(dp[N])%10007)
