n=int(input())
ns=[0 for _ in range(10001)]
dp=[0 for _ in range(10001)]
for i in range(1,n+1):
    ns[i]=int(input())
dp[1]=ns[1]
dp[2]=ns[1]+ns[2]
dp[3]=max(ns[1]+ns[2],ns[1]+ns[3],ns[2]+ns[3])
for i in range(4,n+1):
    dp[i]=max(ns[i]+ns[i-1]+dp[i-3], ns[i]+dp[i-2],dp[i-1])
print(dp[n])