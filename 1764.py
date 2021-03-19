# 듣도 보도 못한 사람 명단 구하기
n, m = map(int, input().split())
# 집합 교집합으로 가자ㅏ
a, b = set(), set()

for i in range(n):
    a.add(input())

for i in range(m):
    b.add(input())
c = a.intersection(b)
c = sorted(list(c))

print(len(c))
for i in c:
    print(i)