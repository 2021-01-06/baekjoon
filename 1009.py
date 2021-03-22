# 분산처리
# a ** b이면 숫자가 어마어마하네
# 무식하게 풀어볼까
# 구현

# n =  int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#
#     c = str(a ** b)
#     if c[-1] == '0':
#         print(10)
#     else:
#         print(int(c[-1]))
# 역시 시간초과

# 10의 자리수 이상은 관심없음

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a ** 2) % 10)
    else:
        b = b % 4
        if b == 1:
            print(a)
        elif b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)