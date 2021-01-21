# sort(key=lambda) 이용한 정렬
import sys
n = int(sys.stdin.readline().strip())
li = []
for i in range(n):
    word = sys.stdin.readline().strip()
    word_len = len(word)
    li.append((word, word_len))

li = list(set(li))
li.sort(key=lambda x: (x[1], x[0]))
for x in li:
    print(x[0])