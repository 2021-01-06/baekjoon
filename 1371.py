# dict을 쓰자
my_dict = dict()
for i in range(26):
    my_dict.setdefault(chr(ord('a')+i), 0)

while True:
    try:
        s = input().strip()
        for i in s:
            if i in my_dict:
                my_dict[i] += 1
    except EOFError:
        break

dict_max = max(my_dict.values())
for k, v in my_dict:
    if v == dict_max:
        print(k)
        break