import sys,copy
def promising(a, c):
    if len(a)==0:
        return True
    r=len(a)
    for i in range(len(a)):
        if c==a[i] or abs(a[i]-c)==r-i:
            return False
    return True
def dfs(a):
    global cnt
    if len(a)==N:
        cnt+=1
        return
    for c in range(N):
        if promising(a, c):
            a.append(c)
            dfs(a)
            a.pop()

N = int(sys.stdin.readline().strip())
cnt=0
dfs([])
print(cnt)