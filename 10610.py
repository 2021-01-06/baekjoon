# 수학적 지식이 필요함
# 일의 자리수가 0
# 각 자리숫자들의 합이 3으로 나누어지면 3의 배수

N = list(input())
N.sort(reverse=True)
# 각 자리의 합
sum = 0
for i in N:
    sum += int(i)

if not (sum%3 == 0) or N[-1] != '0':
    print(-1)
else:
    print(''.join(N))