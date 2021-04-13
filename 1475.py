# # 6과 9는 따로 다룬다
# s = input()
# t = 0
# s_n = 0
# for i in s:
#     if i == '6' or i == '9':
#         s_n += 1
#     else:
#         t += 1
# print(t + (s_n+1)//2)
from collections import defaultdict
test = input()

my_dict = defaultdict(int)
for i in test:
    if i == '9':
        my_dict['6'] += 1
    else:
        my_dict[i] += 1
my_dict['6'] = (my_dict['6']+1)//2
print(max(my_dict.values()))