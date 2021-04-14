# 출석..
at = [0] * 31

for i in range(28):
    at[int(input())] = 1
ze = at.index(0)
ne = at.index(0, ze+1)
nne = at.index(0, ne+1)
print(ne, nne, sep='\n')