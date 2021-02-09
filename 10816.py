input()
ns=list(map(int, input().split()))
input()
ms=list(map(int, input().split()))

def binarysearch(n,m):
    l,h=0,len(n)-1
    while l<=h:
        mid=(l+h)//2
        if n[mid]==m:
            i,j=1,1
            while mid-i>=l:
                if n[mid-i]!=n[mid]:
                    break
                else:
                    i+=1
            while mid+j<=h:
                if n[mid+i]!=n[mid]:
                    break
                else:
                    j+=1
            return i+j-1
        elif n[mid]<m:
            l=mid+1
        elif n[mid]>m:
            h=mid-1
    else:
        return 0
ans =[]
ns.sort()
for m in ms:
    ans.append(binarysearch(ns,m))
print(*ans)