li = []
for x in range(9):
    t = int(input())
    li.append(t)

max, max_id = li[0], 0
for n in range(9):
    if li[n] > max:
        max_id = n
        max = li[n]
print(max, max_id+1, sep="\n")
