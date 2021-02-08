dp=[-1 for i in range(1000001)]
n=int(input())
dp[1],dp[2]=1,2
for i in range(3,1000001):
    dp[i]=(dp[i-1]+dp[i-2])%15746
print(dp[n]%15746)