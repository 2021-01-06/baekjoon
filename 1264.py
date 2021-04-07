# 모음 출력
while True:
    s = input()
    v_n = 0
    if s == '#':
        break
    for i in s:
        if i in 'aeiouAEIOU':
            v_n += 1
    print(v_n)