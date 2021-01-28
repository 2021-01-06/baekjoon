import sys

while True:
    a, b = map(int,sys.stdin.readline().split())
    if not(a or b):
        break
    result = 0
    if not(b%a):
        result='factor'
    elif not(a%b):
        result='multiple'
    else:
        result='neither'
    print(result)

