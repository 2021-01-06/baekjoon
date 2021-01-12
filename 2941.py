import sys
word = sys.stdin.readline().strip()
dic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in dic:
    word = word.replace(x, '1')
print(len(word))