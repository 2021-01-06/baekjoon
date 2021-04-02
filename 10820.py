# 소문자, 대문자, 숫자, 공백
# 죽 돌면서 확인하면 될듯?
# 함수쳌

while True:
    s_c = 0
    c_c = 0
    n_c = 0
    w_c = 0
    try:
        s = input()
        for i in s:
            if i.islower():
                s_c += 1
            elif i.isupper():
                c_c += 1
            elif i.isnumeric():
                n_c += 1
            else:
                w_c += 1
        print(s_c, c_c, n_c, w_c)
    except EOFError:
        break