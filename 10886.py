# 이상한 문제군
n = int(input())
iscute = False
s = []
for i in range(n):
    s.append(int(input()))
if sum(s) > len(s) // 2:
    iscute = True
if iscute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")