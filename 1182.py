# 브루투스 구현
# N개의 정수로 이루어진 수열이 주어지면 합이 S이게 되는 경우의 수를 출력
# 결국 다 봐야하이깐 브루투스 ㅜㅜ
# 시간제한 2초
# N <= 20
N, S = map(int, input().split())
l = list(map(int, input().split()))
c = 0

def d(i, s):
    global c
    if i == N:
        return
    s += l[i]
    if s == S:
        c += 1
    d(i + 1, s - l[i])
    d(i + 1, s)

d(0, 0)
print(c)

