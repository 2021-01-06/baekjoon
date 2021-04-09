# 광고를 하냐 마냐 그것이 문제로다

test_num = int(input())
for _ in range(test_num):
    r, e, c = map(int, input().split())

    if r + c == e:
        print('does not matter')
    elif e - c < r:
        print('do not advertise')
    else:
        print('advertise')