import sys
z=[1,0,1]
o=[0,1,1]
def fibo(n):
    if n>=len(z):
        for i in range(len(z), n+1):
            z.append(z[i-1]+z[i-2])
            o.append(o[i-1]+o[i-2])
    print(z[n],o[n])
test=int(sys.stdin.readline().strip())
for _ in range(test):
    n=int(sys.stdin.readline().strip())
    fibo(n)


