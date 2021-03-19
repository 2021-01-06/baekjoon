n = int(input())
# 문자열을 다루는 문제
# 하나라도 다르면 ?를 넣어야한다
# assign 땜에 리스트로 변경시켜야겠녜
f = list(input().strip())

for i in range(n-1):
    t = input().strip()
    for j in range(len(f)):
        if f[j] != t[j]:
            f[j] = '?'
            # 이게 되나?

print(''.join(f))