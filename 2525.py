# 시계의 원리랑 비슷하네

A, B = map(int, input().split())
C = int(input())
q, r = divmod(B + C, 60)
A, B = (A + q) % 24, r % 60
print(A, B)