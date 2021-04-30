# 완전 제곱수
from math import sqrt as sq
from math import floor as fl
from math import ceil as ce
n = int(input())
m = int(input())

n2 = ce(sq(n))
m2 = fl(sq(m))
t = sum([x**2 for x in range(n2, m2+1)])

if n2 == (m2+1):
    print(-1)
else:
    print(t)
    print(n2**2)