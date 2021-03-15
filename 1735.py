# 두 분수의 합을 기약분수로 나타내시오
# gcd를 써야겠따

def gcd(a, b):
    while b!= 0:
        a, b = b, a%b
    return a

x = list(map(int, input().split()))
y = list(map(int, input().split()))
g = gcd(x[0]*y[1] + x[1]*y[0], x[1]*y[1])
print((x[0]*y[1] + x[1]*y[0])//g, (x[1]*y[1])//g)