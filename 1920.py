import sys
input()
ns=list(map(int, sys.stdin.readline().split()))
input()
ms=list(map(int, sys.stdin.readline().split()))
ns.sort()
def binarysearch(n,a):
    l,h=0,len(n)-1
    while l<=h:
        mid = (l+h) // 2
        if ns[mid]==a:
            print(1)
            break
        elif ns[mid]<a:
            l=mid+1
        elif ns[mid]>a:
            h=mid-1
    else:
        print(0)
for m in ms:
    binarysearch(ns, m)