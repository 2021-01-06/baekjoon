# 앞뒤로 같은 글자 읽기

s = input()
n = len(s) // 2
isp = True
for i in range(n):
    if s[i] != s[len(s)-1-i]:
        isp = False
        break
if isp:
    print(1)
else:
    print(0)