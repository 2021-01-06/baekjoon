# 두 정수 A, B를 받아 A+B를 출력

# 테스트의 갯수
T = int(input())

for _ in range(T):
    A, B = map(int, input().split(','))
    print(A + B)