# 윷놀이를 구현
# 1 : A, 2 : B, 3 : C, 4 : D, 0 : E
my_dict = {1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 0 : 'E'}
for i in range(3):
    rs = 4- sum(list(map(int, input().split())))
    print(my_dict.get(rs))