n=int(input())
ns=[list(map(int, input().split()))for _ in range(n)]

def d(x,y,n):
    global a, b, c
    p=ns[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if ns[i][j]!=p:
                for q in range(3):
                    for w in range(3):
                        d(x+q*n//3,y+w*n//3,n//3)
                return
    if p==-1:
        a+=1
    elif p==0:
        b+=1
    elif p==1:
        c+=1
a,b,c=0,0,0
d(0,0,n)
print(a)
print(b)
print(c)