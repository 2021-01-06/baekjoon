# 단순 수학문제
m = 0
m_id = 0
for i in range(5):
    s = sum(list(map(int, input().split())))
    if s > m:
        m = s
        m_id = i+1
print(m_id, m)