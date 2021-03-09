# 체스판의 흰색위의 말 갯수 세기

c = 0
cp = []
for i in range(8):
    cp.append(input().strip())
    for j in range(8):
        if i % 2:
            if j % 2 == 1 and cp[i][j] == 'F':
                c += 1
        else:
            if j % 2 == 0 and cp[i][j] == 'F':
                c += 1
print(c)
