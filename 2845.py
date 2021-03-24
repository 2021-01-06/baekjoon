l, p = map(int , input().split())
s = list(map(int, input().split()))
w = l * p
for i in s:
    print(i - w, end=' ')
