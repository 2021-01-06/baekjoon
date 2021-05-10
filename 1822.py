# 파이썬의 집합은?
A_num, B_num = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

A_diff_B = A_set - B_set
A_diff_B_num = len(A_diff_B)
if A_diff_B_num == 0:
    print(0)
else:
    print(len(A_diff_B))
    print(*sorted(A_diff_B))