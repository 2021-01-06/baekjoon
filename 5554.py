# x분 y초
m, s = 0, 0
for _ in range(4):
    s+= int(input())
m, s = divmod(s, 60)
print(m)
print(s)