# gcd와 dfs의 조합
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

l = [0] * 10
def dfs(i, d):
    global s
    if d == 2:
        s += gcd(l[0], l[1])
        return
    for _ in range(i, len(ds)):
        l[d] = ds[_]
        dfs(_+1, d+1)

t = int(input())

for i in range(t):
    ns = list(map(int, input().split()))
    n = ns[0]
    ds = ns[1:]
    s = 0
    dfs(0, 0)
    print(s)