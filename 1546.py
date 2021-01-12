import sys
n = int(input())
li = list(map(int, sys.stdin.readline().split()))
m = max(li)
li_new = [x/m*100 for x in li]
print(sum(li_new)/len(li_new))