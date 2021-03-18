# 암호를 만들어 보쟈
# 암호는 사전순이고
# 딱봐도 dfs로 방문하면 될듯
# L은 암호의 길이
# C는 주어진 문자갯수
# 경우를 생각안했네
# 나중에 다시


# L, C = map(int, input().split())
# s = list(input().split())
#
# # 정렬
# s.sort()
# l = [0] * C
# def dfs(i, d, v, w):
#     if d == 4:
#         if v >= 1 and w >= 2:
#             for i in range(L):
#                 print(l[i], end='')
#             print()
#             print(v, w)
#         return
#     for _ in range(i, len(s)):
#         l[d] = s[_]
#         if s[_] in 'aeiou':
#             v += 1
#         else:
#             w += 1
#         # 시작점 올리기, 깊이 상승
#         dfs(_+1, d+1, v, w)
#
#
# dfs(0, 0, 0, 0)

# 모음이 최소 하나 자음이 최소 둘
# 다 뜯어 고쳐야겠는데?
# 백트랙하기가 힘드네