n=int(input())
ls=list(map(int,input().split()))
ps=list(map(int,input().split()))
c=0
l,p=ls[0],ps[0]
c+=l*p
for i in range(1,len(ps)-1):
    if ps[i]<p:
        p=ps[i]
    c+=p*ls[i]
print(c)

