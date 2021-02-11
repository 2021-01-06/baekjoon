n=int(input())
ns=[0]
ns.extend(list(map(int,input().split())))
dp=[0 for _ in range(1001)]
for i in range(1,n+1):
    for j in range(1,i):
        if ns[i]>ns[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))