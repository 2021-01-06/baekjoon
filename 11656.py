S = input()

sl = []

for i in range(len(S)):
    sl.append(S[i:])



sl.sort()

for i in sl:
    print(i)