# 구현문제
import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

n = 0
# 총감독은 적어도 한명
n += len(a)

# 부 감독들 일하자
for i in a:
    i -= b
    if i < 0:
        continue
    n += math.ceil(i / c)
print(n)
