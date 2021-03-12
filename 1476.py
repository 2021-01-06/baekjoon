# 이상한 날짜의 날짜
# data format : (E, S, M)
# properties : n 이 주어지면 E = n % 16, S = n % 29, M = n % 20의 특징을 가짐
# return n

# 15 * 29 * 19 n은 최대 7980이네

# 무식한 코딩
# 2초 메모리 4M
c = 1
e, s, m = map(int, input().split())
while True:
    #
    if (c-e) % 15 == 0 and (c-s) % 28 == 0 and (c-m) % 19 == 0:
        print(c)
        break
    c += 1