# 알파벳 사이의 거리

n = input()
for _ in range(5):
    s1, s2 = input().split()
    result = []
    for i in range(len(s1)):
        a1, a2 = ord(s1[i]), ord(s2[i])
        diff = a2-a1
        if a2 < a1:
            diff += 26
        result.append(diff)
    print('Distances:', *result)