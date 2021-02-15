import heapq
import sys
n=int(sys.stdin.readline())
h=[]
for _ in range(n):
    o=int(sys.stdin.readline())
    if o==0:
        if len(h)==0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h,(-o,o))
