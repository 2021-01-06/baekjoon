# 규칙이 돌은 1개 또는 3개 가져간다
# 상근먼저 시작
# n == 1 상근 1
# n == 2 창영 1 1
# n == 3 상근 3
# n == 4 창영 1 3 3 1
# n == 5
# 번갈아서 되나?

n = int(input())
print('SK' if n % 2 else 'CY')