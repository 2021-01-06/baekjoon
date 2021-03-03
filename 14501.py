# 퇴사라니
# 입력
N = int(input())
s = [list(map(int, input().split())) for i in range(N)]
dp = []

# 그리디 한 방법은 아니고,,, 브루투스 되겠네
# 다이나믹으로 ㄱㄱ
# dp에는 N일 까지의 최대수입

