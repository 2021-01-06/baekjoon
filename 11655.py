s = input()
s = s.lower()

dic = [chr(i+ord('a')) for i in range(0, 26)]
n_s = []
for i in s:
    if 'a' <= s <= 'z':
        n_s.append(dic((ord(i)-ord('a')+13)%26))
    else:
        n_s.append(i)
n_s = ''.join(n_s)
print(n_s)