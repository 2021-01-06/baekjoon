# dict의 활용이다
my_dict = dict()

after = [chr(ord('A')+i) for i in range(26)]
before = [chr(ord('A')+(i+3)) for i in range(23)]
before.append('A')
before.append('B')
before.append('C')
for k, v in zip(before, after):
    my_dict[k] = v

test = input()

for i in test:
    print(my_dict[i], end='')