import statistics
import heapq
import sys
n=int(sys.stdin.readline())
l,r=[],[]

for _ in range(n):
    o=int(sys.stdin.readline())
    if len(l)==len(r):
        heapq.heappush(l,(-o,o))
    else:
        heapq.heappush(r,(o,o))
    if r and l[0][1]>r[0][1]:
        a=heapq.heappop(l)[1]
        b=heapq.heappop(r)[1]
        heapq.heappush(l,(-b,b))
        heapq.heappush(r,(a,a))
    print(l[0][1])