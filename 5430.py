from collections import deque

t=int(input())
for _ in range(t):
    os=input()
    input()
    ns=input().strip('[]\n')
    try:
        ns=deque(map(int,ns.split(',')))
    except:
        pass
    rf=False
    ef=False
    for o in os:
        if o=='R':
            rf=not rf
        elif o=='D':
            if len(ns)==0:
                print('error')
                ef=True
                break
            if rf:
                ns.pop()
            else:
                ns.popleft()
    if rf and not ef:
        print(list(reversed(ns)))
    elif not rf and not ef:
        print(list(ns))