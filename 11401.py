p=1000000007
def m(a, n):
    if n%2:
        return m(a,n-1)*a
    elif n==0:
        return 1
    elif n==1:
        return a
    else:
        return (m(a,n//2)**2)%p


n,k=map(int,input().split())

A,B=1,1
for i in range(1,n+1):
    A*=i
    A%=p
for i in range(1,k+1):
    B*=i
    B%=p

for i in range(1,n-k+1):
    B*=i
    B%=p

ans=(A*m(B,(p-2)))%p
print(ans)