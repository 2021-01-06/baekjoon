# 이진트리에서
# 맨 오른쪽 값이네
# but 수학적으로 쉽게 구현가능할 듯
# 주어진대로 구현해보기

x = int(input())
l = 64
s = 64
c = 1
while x != s:
    l = l // 2
    if s - l >= x:
        s -= l
    else:
        c += 1
print(c)
