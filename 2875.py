# 팀을 결정하는건 적은수가 결정한다
from math import ceil as ce
n, m, k = map(int, input().split())

n_2 = n // 2
m_2 = m // 1
if n_2 < m_2:
    mi = n_2
else:
    mi = m_2
n_re = n - mi*2
m_re = m - mi*1

k -= n_re
k -= m_re
if k < 0: k = 0
k = ce(k / 3)

print(min(n_2, m_2) - k)
