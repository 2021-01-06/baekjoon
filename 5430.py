import sys
from collections import deque

test_num = int(sys.stdin.readline().strip())
for i in range(test_num):
    orders=sys.stdin.readline().strip()
    num=int(sys.stdin.readline().strip())
    num_li= deque(sys.stdin.readline().strip('[]\n').split(','))
    result_li=[]
    error=False
    is_reverse = False
    if num ==0:
        error=True
        print("error")
    for order in orders:
        if order=='R':
            is_reverse = not is_reverse
        elif order=='D':
            if len(num_li)==0:
                print("error")
                error=True
                break
            else:
                if is_reverse:
                    num_li.pop()
                else:
                    num_li.popleft()
    if not error:
        if is_reverse:
            print(list(reversed(list(map(int, num_li)))))
        else:
            print(list(map(int, num_li)))
