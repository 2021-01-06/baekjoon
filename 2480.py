# set을 쓰면 편할듯?
i = list(map(int, input().split()))
s = set(i)
if len(s) == 1:
    print(10000 + max(s)*1000)
elif len(s) == 3:
    print(max(s)*100)
# 따로 처리해야하넴..
else:
    for _ in s:
        if i.count(_) == 2:
            print(1000 + _*100)
