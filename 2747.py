# n <= 45 인 자연수에 대한 fibo(n)
fibo = [0] * 46
for i in range(1, 3):
    fibo[i] = 1
for i in range(3, 46):
    fibo[i] = fibo[i-1] + fibo[i-2]

n = int(input())
print(fibo[n])