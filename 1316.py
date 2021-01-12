import sys
n = int(sys.stdin.readline().strip())
cnt = 0
for r in range(n):
    word = sys.stdin.readline().strip()
    alpha = list(set(word))
    for x in alpha:
        if word.find(x) + word.count(x) != word.rfind(x) + 1:
            cnt += 1
            break
print(n-cnt)

