n=int(input())
ns=list(map(int,input().split()))
s=[ns[0]]
for i in range(len(ns)-1):
    s.append(max(ns[i+1]+s[i],ns[i+1]))
print(max(s))