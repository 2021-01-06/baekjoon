p=1000000007
def t(g,n):
    if n==1:
        return g
    elif n%2:
        return m(t(g,n-1),g)
    else:
        return t(m(g,g),n//2)
def m(a,b):
    c=[[0]*len(b[0]) for i in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            for k in range(2):
                c[i][j]+=a[i][k]*b[k][j]
            c[i][j]%=p
    return c
n=int(input())
g=[[1,1],[1,0]]
s=[[1],[1]]
if n<3:
    print(1)
else:
    print(m(t(g,n-2),s)[0][0])