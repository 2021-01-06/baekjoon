# 수 이어쓰기
# 9  90*2  900*3
n = input()
i = 0
a = 0
while i < len(n)-1:
    a += 9 * (10 ** i) * (i+1)
    i += 1
a +=  (int(n) - (10 ** (len(n)-1)) + 1) *len(n)
print(a)