K, N, M = map(int, input().split())
money = K*N-M
print(money if money >= 0 else 0)