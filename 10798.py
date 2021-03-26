s = [[] for i in range(15)]

for i in range(5):
    t = input().strip()
    for j in range(len(t)):
        s[j].append(t[j])

for i in range(15):
    if i == []:
        break
    print(''.join(s[i]), end='')
