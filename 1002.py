import sys

test_num = int(sys.stdin.readline().strip())

for _ in range(test_num):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    r_sum = abs(r2+r1)
    r_diff = abs(r2-r1)
    d = (abs(x2-x1)**2+abs(y2-y1)**2)**(1/2)

    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == r_sum or d == r_diff:
            print(1)
        elif r_diff < d < r_sum:
            print(2)
        else:
            print(0)