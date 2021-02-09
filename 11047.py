n, k=map(int, input().split())
a=[int(input()) for _ in range(n)]
w=0
for p in list(reversed(a)):
    w+=k//p
    k-=p*(k//p)
    if k==0:
        break
print(w)