# 이진수 연산

# 참고
A = int(input(), 2)
B = int(input(), 2)
n = 100000
mask = 2 ** n - 1

print(f'{A&B:0{n}b}')
print(f'{A|B:0{n}b}')
print(f'{A^B:0{n}b}')
print(f'{mask-A:0{n}b}')
print(f'{mask-B:0{n}b}')