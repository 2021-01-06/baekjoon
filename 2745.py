# B진법 수 N을 10 진법으로 출력
# 내장함수가 지원하려나?
# 지원안함
s, n = input().split()
n = int(n)
r = 0
for idx, k in enumerate(s):
    t = 0
    if ord('0') <= ord(k) <= ord('9'):
        t = ord(k) - ord('0')
    elif ord('A') <= ord(k) <= ord('Z'):
        t = ord(k) - ord('A') + 10
    r +=  t * n ** (len(s)-idx-1)
print(r)