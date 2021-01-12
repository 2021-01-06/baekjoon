def self_num():
    ori_set = set(range(1, 10001))
    gen = set()
    for i in range(1, 10001):
        cnt = 0
        for j in range(len(str(i))):
            cnt += int(str(i)[j])
        gen.add(i + cnt)
    my_set = ori_set - gen
    for num in sorted(my_set):
        print(num)

self_num()