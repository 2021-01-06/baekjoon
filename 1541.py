ns=input().split('-')
for i in range(len(ns)):
    n=0
    ts=ns[i].split('+')
    for t in ts:
        n+=int(t)
    ns[i]=str(n)
ns='-'.join(ns)
print(eval(ns))
