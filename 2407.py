# nCm을 출력한다
# nCm = n! // (n-m)!m!
# n <= 100 이므로 동적으로 하면 될듯?
# 피보나치랑 헷갈렸네 ㅋㅋ

# f

def f(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
dp = [0] * 101
dp[0] = 1

for i in range(1, 100+1):
    dp[i] = dp[i-1] * i

n, m = map(int, input().split())
print(dp[n]//dp[n-m]//dp[m])
