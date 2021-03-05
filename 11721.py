# 길이가 N인 문자열을 10자씩 끊어서 출력
n = 10
s = input()
for i in range(0, len(s)):
    if i != 0 and i % 10 == 0:
        print()
    print(s[i], end = '')