
test_num = int(input())

for _ in range(test_num):
    car_price = int(input())
    option_num = int(input())
    option_price = 0
    for i in range(option_num):
        a, b = map(int, input().split())
        option_price += a*b
    print(car_price+option_price)