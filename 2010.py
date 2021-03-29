# 조금 끄젹여 보면
# 그리디하고
# 콘센트 갯수만큼 다 더하고 n-1을 뺀다
import sys
N = int(sys.stdin.readline())
s = 0

for i in range(0, N):
    s += int(sys.stdin.readline())
print(s-(N-1))