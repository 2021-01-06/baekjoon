x = int(input())
n, x_new = 0, x
while True:
    n = n + 1
    x_new = (x_new % 10) * 10 + ((x_new % 10) + int((x_new % 100 - x_new % 10) / 10)) % 10
    if x == x_new:
        print(n)
        break