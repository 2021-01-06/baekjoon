# 단순 빼기 실생활 문제

total = int(input())
li = []

for i in range(9):
    li.append(int(input()))

result = total - sum(li)
print(result)