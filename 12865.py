n,k=map(int,input().split())
w,v=[0],[0]
for _ in range(n):
    tw,tv=map(int,input().split())
    w.append(tw)
    v.append(tv)

dp=[[0 for i in range(k+1)]for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if w[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
print(dp[n][k])