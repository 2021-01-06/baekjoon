# 정렬하기

test_num = int(input())

ns = []
for i in range(test_num):
    ns.append(int(input()))

ns.sort(key=lambda x:-x)
for i in ns:
    print(i)