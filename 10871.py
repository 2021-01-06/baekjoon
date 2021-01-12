import sys
a, b = map(int, sys.stdin.readline().split())
squ = list(map(int,sys.stdin.readline().split()))
new_squ = list(filter(lambda x: x < b, squ))
for x in new_squ:
    print(x, end=" ")