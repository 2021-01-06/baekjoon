# 이친수를 구하기
# 어감이 이상하네
# f(n) 에 대헤 n자리 이진수가 0 으로 끝나는 경우와 1로 끝나는 경우
# 0으로 끝나는 경우는 f(n-1)에서 0을 붙이면 나옴
# 1로 끝나는 경우는 f(n-2)에서 01을 붙이면 나옴
# 이게 끝?
# 한번 해보고 말해

fn = [0] * 91
n = int(input())

for i in range(1, 3):
    fn[i] = 1
for i in range(3, 91):
    fn[i] = fn[i-1] + fn[i-2]

# 걍 피보나치네 ..
print(fn[n])
