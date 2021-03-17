# 결국 한번씩 다봐야 한다
# n
flag = False
min = float('inf')
sum = 0
for i in range(7):
    n = int(input())
    if n % 2:
        sum += n
        flag = True
        if n < min:
            min = n
if flag:
    print(sum)
    print(min)
else:
    print(-1)