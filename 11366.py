# 뒤집기

while True:
    s = input()
    if s == 'END':
        break
    else:
        for i in reversed(s):
            print(i, end='')
        print()