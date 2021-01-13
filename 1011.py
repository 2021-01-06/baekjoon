import sys
test = int(sys.stdin.readline().strip())
for i in range(test):
    x, y = map(int, sys.stdin.readline().split())
    dis = y - x
    n, move_sum = 0, 0
    move = 1
    while move_sum < dis:
        n += 1
        move_sum += move
        if n % 2 == 0:
            move += 1
    print(n)