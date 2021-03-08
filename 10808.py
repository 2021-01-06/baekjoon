# 문자열안에 있는 알파벳의 갯수를 세기
s = input().strip()

l = [0] * 26

for i in s:
    l[ord(i) - ord('a')] += 1

for i in l:
    print(i, end = ' ')