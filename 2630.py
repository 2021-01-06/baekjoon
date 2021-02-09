import sys
n=int(sys.stdin.readline().strip())
nn=[list(map(int, sys.stdin.readline().split()))for i in range(n)]
wc,bc=0,0
def f(a,b,n):
    global wc,bc
    p=nn[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if p!=nn[i][j]:
                f(a,b,n//2)
                f(a,b+n//2,n//2)
                f(a+n//2,b,n//2)
                f(a+n//2,b+n//2,n//2)
                return
    if p:
        bc+=1
        return
    else:
        wc+=1
        return

f(0,0,n)
print(wc,bc,sep='\n')