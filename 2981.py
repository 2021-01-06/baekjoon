import sys,math
test=int(sys.stdin.readline().strip())
test_num=[int(sys.stdin.readline().strip()) for x in range(test)]
test_num.sort()
for x in range(test-1):
    if x==0:
        gcd=test_num[1]-test_num[0]
    else:
        gcd=math.gcd(gcd, test_num[x+1]-test_num[x])
result=[]
for x in range(2, int(gcd**(1/2))+1):
    if gcd%x==0:
        result.append(x)
        result.append(gcd//x)
result.append(gcd)
result=list(set(result))
result.sort()
print(*result)