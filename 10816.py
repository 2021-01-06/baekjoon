input()
ns=list(map(int,input().split()))
input()
ms=list(map(int,input().split()))
d=dict()
for n in ns:
    if n not in d:
        d[n]=1
    else:
        d[n]+=1
r=[]
for m in ms:
    if m in d:
        r.append(d[m])
    else:
        r.append(0)
print(*r)