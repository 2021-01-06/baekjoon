import heapq
import sys
h=[]
n=int(sys.stdin.readline())
for _ in range(n):
    o=int(sys.stdin.readline())
    if o==0:
        if len(h)==0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
            heapq.heappush(h,o)