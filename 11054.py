n=int(input())
ns=list(map(int,input().split()))
dpl=[0 for i in range(n)]
dpr=[0 for i in range(n)]
dpb=[0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if ns[i]>ns[j] and dpl[j]>dpl[i]:
            dpl[i]=dpl[j]
    dpl[i]+=1

for i in range(n-1, -1, -1):
    for j in range(n-1, i-1, -1):
        if ns[i]>ns[j] and dpr[j]>dpr[i]:
            dpr[i]=dpr[j]
    dpr[i]+=1

for i in range(n):
    dpb[i]=dpr[i]+dpl[i]-1

print(max(dpb))