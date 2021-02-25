# 피보나치 n 을 구하는 프로그램
# n <=90 이므로 동적으로 합시당
fibo = [0] * 91

# 시작 값들 입력
fibo[1] = 1
fibo[2] = 1

# fn = fn-1 + fn-2 그대로 적용
for i in range(3, 91):
    fibo[i] = fibo[i-1] + fibo[i-2]

n = int(input())
print(fibo[n])