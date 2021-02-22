m,n=map(int, input().split())
a=[]
for i in range(m):
    a.append(list(map(int, input().split())))
def m_m(a,b):
    m=len(a)
    c = [[0 for i in range(m)] for j in range(m)]
    for i in range(m):
        for j in range(m):
            for _ in range(m):
                c[i][j] += a[i][_] * b[_][j]
            c[i][j]%=1000
    return c
def m(a,n):
    if n==1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j]%=1000
        return a
    elif n==0:
        return a
    elif n%2:
        return m_m(a,m(a,n-1))
    else:
        return m(m_m(a,a),n//2)

c=m(a,n)
for i in range(len(a)):
    print(*c[i])