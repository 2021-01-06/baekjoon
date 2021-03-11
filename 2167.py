# 2차원 배열에서 원하는곳에서
# 원하는 곳까지의 배열합 구하기
n, m = map(int, input().split())

ns = [list(map(int, input().split())) for i in range(n)]

k = int(input())

# for문 2개를 돌아서 시간초과
for _ in range(k):
    i, j, x, y = map(int, input().split())
    s = 0

    for a in range(i-1, x):
        for b in range()