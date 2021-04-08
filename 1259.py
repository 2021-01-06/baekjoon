

while True:
    s = input()
    r = 'yes'
    if s == '0':
        break
    else:
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                r = 'no'
                break
        print(r)