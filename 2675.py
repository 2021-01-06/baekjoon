case = int(input())
for i in range(case):
    n, st = input().split()
    result = ""
    for i in st:
        result += i*int(n)
    print(result)