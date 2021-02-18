n=int(input())
ns=[]
for _ in range(n):
    ns.append(list(map(int,input().split())))
dp=[0 for i in range(n)]
ns.sort(key=lambda x:x[0])
for i in range(n):
    for j in range(i):
        if ns[i][1]>ns[j][1] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(n-max(dp))