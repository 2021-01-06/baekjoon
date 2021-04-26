n = int(input())
f = int(input())

processed_n = n // 100 * 100
to_add = 0

for _ in range(100):
    test_n = processed_n + to_add
    if test_n % f == 0:
        break
    to_add += 1

if to_add < 10:
    print(0, to_add, sep='')
else:
    print(to_add)