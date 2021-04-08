
# 입력
N = int(input())
t = []
p = []
dp = [0] * (N+1)

for i in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(N-1, -1, -1):
    if i + t[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])

print(dp[0])