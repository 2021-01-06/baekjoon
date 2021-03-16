# 단어를 숫자로 치환해서 최댓값을 구하자
# 알파벳은 총 26개이다

# 입력
n = int(input())
s = []
for i in range(n):
    s.append(list(input().strip()))

a = [0] * 26
# 그리디 하게 접근해야하는데..
# 우짜지..
# 치트키
for i in s:
    li = len(i)
    for j in range(li):
        # 높은 자리수의 10의 배수로 치환
        a[ord(i[j]) - 65] += 10 ** (li-j-1)
a.sort(reverse=True)
r = 0
c = 9
for i in a:
    r += c * i
    c -= 1
print(r)