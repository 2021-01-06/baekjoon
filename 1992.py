# 입력
# 조건
# 결과

n=int(input())
nn=[input().strip() for _ in range(n)]
s=[]
def w(a,b,n):
    p=nn[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if p!=nn[i][j]:
                s.append('(')
                w(a,b,n//2)
                w(a,b+n//2,n//2)
                w(a+n//2,b,n//2)
                w(a+n//2,b+n//2,n//2)
                s.append(')')
                return
    s.append(p)
    return
w(0,0,n)
print(''.join(s))
