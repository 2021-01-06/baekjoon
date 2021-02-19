a,b,c=map(int, input().split())

def d(a,b):
    if b%2:
        return d(a,b-1)*a
    elif b==0:
        return 1
    elif b==1:
        return a
    else:
        x=d(a,b//2)
        return x*x%c

print(d(a,b)%c)