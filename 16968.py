# 차량 번호판



my_dict = {'c' : 26, 'd' : 10}

my_car = input()
n = len(my_car)

first = my_dict[my_car[0]]
for i in range(1, n):
    mul = my_dict[my_car[i]]
    if my_car[i-1] == my_car[i]:
        mul -= 1
    first *= mul
print(first)