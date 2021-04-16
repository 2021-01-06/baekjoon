test_num = int(input())

for _ in range(test_num):
    s = input()
    test_s = int(s[-1])
    if test_s%2:
        print('odd')
    else:
        print('even')