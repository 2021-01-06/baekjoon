# 암호를 만들어 보쟈
# 암호는 사전순이고
# 딱봐도 dfs로 방문하면 될듯
# L은 암호의 길이
# C는 주어진 문자갯수
# 경우를 생각안했네
# 나중에 다시


L, C = map(int, input().split())
s = list(input().split())

# 정렬
s.sort()
l = [0] * C
def dfs(i, d):
    if d == 4:
        for i in range(L):
            print(l[i], end='')
        print()
        return
    for _ in range(i, len(s)):
        l[d] = s[_]
        # 시작점 올리기, 깊이 상승
        dfs(_+1, d+1)

dfs(0, 0)