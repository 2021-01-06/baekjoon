# 가장 큰경우 5를 다 6으로 봤을때
# 가장 작은 경우 6을 다 5로 봤을때

a, b = input().split()

a = a.replace('6', '5')
b = b.replace('6', '5')
print(int(a)+int(b), end=' ')

a = a.replace('5', '6')
b = b.replace('5', '6')
print(int(a)+int(b))
