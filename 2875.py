# 팀을 결정하는건 적은수가 결정한다
n, m, k = map(int, input().split())
diff = abs(n - m)
n = n // 2
k = k - diff
print()
