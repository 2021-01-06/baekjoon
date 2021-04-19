# strip을 쓰면 되겠네?

a, b = input().split()

a = a[::-1].lstrip('0')
b = b[::-1].lstrip('0')
print(str(int(a)+int(b))[::-1].lstrip('0'))