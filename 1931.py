n=int(input())
ns=[]
for i in range(n):
    ns.append(list(map(int, input().split())))
ns.sort()
ns.sort(key=lambda x:x[1])
c=0
s=0
for a,b in ns:
    if a>=s:
        c+=1
        s=b
print(c)