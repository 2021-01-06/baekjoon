# n,m=map(int, input().split())
# a,b=[],[]
# for i in range(n):
#     a.append(list(map(int, input().split())))
# m,k=map(int, input().split())
# for i in range(m):
#     b.append(list(map(int, input().split())))
# c=[[0 for i in range(k)]for j in range(n)]
#
# for i in range(n):
#     for j in range(k):
#         for _ in range(m):
#             c[i][j]+=a[i][_]*b[_][j]
#
# for i in range(n):
#     print(*c[i])
import numpy as np

n,m=map(int, input().split())
a,b=[],[]
for i in range(n):
    a.append(list(map(int, input().split())))
m,k=map(int, input().split())
for i in range(m):
    b.append(list(map(int, input().split())))
c=[[0 for i in range(k)]for j in range(n)]
a=np.array(a).reshape(n,m)
b=np.array(b).reshape(m,k)
c=a.dot(b)
for i in range(len(c)):
    print(*c[i])