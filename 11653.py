import sys

n = int(sys.stdin.readline().strip())

while n != 1:
    for j in range(2, n+1):
        if n % j == 0:
            n = n // j
            print(j)
            break