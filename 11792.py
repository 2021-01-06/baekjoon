import sys


def hanoi(n, fr, tmp, to, li):
    if n == 1:
        li.append((fr, to))
        return
    hanoi(n-1, fr, to, tmp, li)
    li.append((fr, to))
    hanoi(n-1, tmp, fr, to, li)


n = int(sys.stdin.readline().strip())
li, k = [], 2 ** n -1
hanoi(n, 1, 2, 3, li)
print(k)
for (a, b) in li:
    print(a, b)