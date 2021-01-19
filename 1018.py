import sys

m, n = map(int, sys.stdin.readline().split())
# 문자열로 입력
board = []

for _ in range(m):
    board.append(sys.stdin.readline().strip())

# a, b는 보드선텍 인덱스
cnt_li = []
for a in range(m-7):
    for b in range(n-7):
        cnt_b = 0
        cnt_w = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                # 첫번째가 W일때 짝수에는 W 홀수에는 B
                if (i+j) % 2:
                    if board[i][j] != 'B':
                        cnt_w += 1
                    if board[i][j] != 'W':
                        cnt_b += 1
                else:
                    if board[i][j] != 'W':
                        cnt_w += 1
                    if board[i][j] != 'B':
                        cnt_b += 1
        cnt_li.append(cnt_w)
        cnt_li.append(cnt_b)


print(min(cnt_li))