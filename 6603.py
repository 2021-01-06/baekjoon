# dfs를 통해 조건이 완료되면 빠져나오고
# 앞에서 부터 깊이 들어가본다

# dfs의 변수는 시작점과 깊이
# 깊이는 엔드조건
# 시작점은 변하는것
def dfs(s, d):
    # 깊이가 6 이꼴 갯수가 6개
    if d == 6:
        # 6개를 찾았으면
        for i in range(6):
            print(k[i], end=' ')
        print()
        return
    for i in range(s, len(ns)):
        k[d] = ns[i]
        # 시작점 올리기, 깊이 상승
        dfs(i+1, d+1)
# 입력 받기
# k값을 미리 배열에 지정해놈
k = [0 for i in range(6)]
while True:
    ns = list(map(int, input().split()))
    if ns[0] == 0:
        break
    ns.pop(0)
    # 시작
    dfs(0, 0)
    print()
