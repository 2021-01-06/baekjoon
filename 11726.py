fb=[0]*1001
for i in range(3):
    fb[i]=i
for i in range(3,1001):
    fb[i]=fb[i-1]+fb[i-2]
    fb[i]%=10007
n=int(input())
print(fb[n])

