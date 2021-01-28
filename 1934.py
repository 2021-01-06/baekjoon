import sys,math
test=int(sys.stdin.readline().strip())
for t in range(test):
    a,b=map(int,sys.stdin.readline().split())
    lcd = a*b//math.gcd(a, b)
    print(lcd)