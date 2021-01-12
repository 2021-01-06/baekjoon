a, b, c = int(input()), int(input()), int(input())
li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = a * b * c
for x in range(len(str(n))):
    li[int(str(n)[x])] = li[int(str(n)[x])] + 1
print(*li)
