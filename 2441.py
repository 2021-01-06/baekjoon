# 별 ㄱ 자로 출력하기
n = int(input())

for i in range(n, 0, -1):
    s = ' ' * (n - i) + '*' * i
    print(s)
