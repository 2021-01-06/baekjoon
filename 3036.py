import sys, math
test=int(sys.stdin.readline().strip())
numbers=list(map(int, sys.stdin.readline().split()))
for i in range(1, test):
    gcd = math.gcd(numbers[0],numbers[i])
    print("{}/{}".format(numbers[0]//gcd, numbers[i]//gcd))

