# 동적

n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
dp = [0] * (n+1)
# dp[n]은 n개의 카드일 때 최댓값
# dp[1] 카드 한개 뽑을때 최댓값 -> p[1]
# dp[2] 카드 두개 뽑을때 최댓값 -> dp[1] + p[1] or p[2]
# dp[3] 카드 세개 뽑을떄 최댓값 -> dp[1] + p[2] or dp[2] + p[1] or p[3]
dp[1] = p[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + p[j]:
            dp[i] = dp[i-j] + p[j]
print(dp[n])