import sys, math
# 5C4 같은경우
def get_5(n):
    cnt=0
    while n!=0:
        n=n//5
        cnt+=n
    return cnt
def get_2(n):
    cnt=0
    while n!=0:
        n=n//2
        cnt+=n
    return cnt
n, m=map(int, sys.stdin.readline().split())
print(min(get_5(n)-get_5(m)-get_5(n-m), get_2(n)-get_2(m)-get_2(n-m)))