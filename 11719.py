# 똑같은 문제같은데
while True:
    try:
        print(input())
    except EOFError:
        break