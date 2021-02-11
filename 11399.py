n=int(input())
ns=list(map(int, input().split()))
ns.sort()
t,c=0,0
for n in ns:
    c+=n
    t+=c
print(t)
