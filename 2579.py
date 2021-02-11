import sys
n=int(sys.stdin.readline().strip())
ss=[0 for i in range(300)]
dp=[0 for i in range(300)]
for i in range(n):
    ss[i]=int(sys.stdin.readline().strip())
dp[0]=ss[0]
dp[1]=ss[1]+dp[0]
dp[2]=max(ss[2]+ss[1],ss[2]+ss[0])
for i in range(3, n):
    dp[i]=max(ss[i]+dp[i-2], ss[i]+ss[i-1]+dp[i-3])
print(dp[n-1])
# index Error?
