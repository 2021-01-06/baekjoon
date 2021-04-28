# 골드바희의 추측
import sys
n=1000000
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2 ,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
primes.remove(2)
a[2] = False
while True:
    test_num = int(sys.stdin.readline())
    if test_num == 0:
        break
    else:
        for i in range(3, n+1):
            if a[i] == True:
                if test_num-i > 0:
                    if a[test_num-i] == True:
                        print(test_num, '=', i, '+', test_num-i)
                        break
        else:
            print("Goldbach's conjecture is wrong.")


