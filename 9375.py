import sys

test=int(sys.stdin.readline().strip())
for _ in range(test):
    n = int(sys.stdin.readline().strip())
    cases = 1
    my_clothes = dict()
    for _ in range(n):
        cloth, cloth_type = sys.stdin.readline().split()
        if cloth_type not in my_clothes:
            my_clothes[cloth_type]=1
        else:
            my_clothes[cloth_type]+=1

    for n in my_clothes.values():
        cases = cases * (n+1)
    cases-=1
    print(cases)