# 1~100
computers = [0] * 101
n = int(input())
checked = list(map(int, input().split()))

count = 0
for i in checked:
    if computers[i]:
        count += 1
    else:
        computers[i] = 1
print(count)