import sys
n = int(input())
for x in range(0, n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print("Case #"+str(x+1)+":", a, "+", b, "=", a+b)


