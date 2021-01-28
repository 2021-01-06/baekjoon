import sys
import math
a, b=map(int,sys.stdin.readline().split())
print(math.gcd(a, b), int(a*b/math.gcd(a,b)),sep='\n')
# math.lcm(a, b) python 3.9부터
