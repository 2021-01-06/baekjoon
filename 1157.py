import sys

str = sys.stdin.readline().strip().upper()
str_alpha = list(set(str))

cnt_li = list()

for alpha in str_alpha:
    cnt = str.count(alpha)
    cnt_li.append(cnt)

if cnt_li.count(max(cnt_li)) > 1:
    print("?")
else:
    print(str_alpha[cnt_li.index(max(cnt_li))])
