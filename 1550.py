# 16 진수의 수를 받아 10진수로

def abc(t):
    if 'A' <= t <= 'F':
        e = 10 + ord(t) - ord('A')
        return int(e)
    else:
        return int(t)

s = 0
li = list(input())
l = len(li)
i = 0
while l:
    s += abc(li[l-1]) * (16 ** i)
    i += 1
    l -= 1
print(s)