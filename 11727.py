# 딱 봐도 피보나치
# n 번에 직사각형을 만드는 경우의 수는  n-2에서 가로 직사각형 2개랑 큰 정사각형
# n-1 에서 세로 직사각형
# f(n) = f(n-2) * 2 + f(n-1)
# 점화식이 나온다
# n < 1000 이므로 동적으로 할당합시당
n = int(input())
dp = [0] * 1001
for i in range(0, 2):
    dp[i] = 1
for i in range(2, 1001):
    dp[i] = (dp[i-2] * 2 + dp[i-1]) % 10007
print(dp[n])