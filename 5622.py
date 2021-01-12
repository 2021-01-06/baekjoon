import sys
word = sys.stdin.readline().strip()
li = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for x in word:
    for y in li:
        if x in y:
            time += (li.index(y) + 3)

print(time)