t=int(input())
fn=[0]*11
fn[1],fn[2],fn[3]=1,2,4
def f(n):
    fn[n]=fn[n-1]+fn[n-2]+fn[n-3]

for n in range(4, 11):
    f(n)
for _ in range(t):
    n=int(input())
    print(fn[n])