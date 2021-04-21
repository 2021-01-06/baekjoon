# sort를 잘이용하자

n = int(input())

a = []
for i in range(n):
    t = input()
    s = 0
    for i in t:
        if '0' <= i <='9':
            s += int(i)
    a.append((t, s))
a.sort(key=lambda x:(len(x[0]), x[1], x[0]))
for b, c in a:
    print(b)