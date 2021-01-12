import sys
t = int(input())

for n in range(t):
    a ,b = map(int, sys.stdin.readline().strip().split())
    print(a+b)