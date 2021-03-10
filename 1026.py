# 작은것과 큰것을 곱해야 최솟값이 출력될 듯
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
s = 0
for i in range(n):
    s += a[i] * b[i]
print(s)