# # 에라토스테네스의 채
# N, K = map(int, input().split())
# # k번째 지워진 수를 출력
# s = [False, False] + [True] * (N-1)
# c = 0
# a = 0
# for i in range(2, N+1):
#     if s[i]:
#         c += 1
#         if c == K:
#             a = j
#         for j in range(2*i, N+1, i):
#             if s[j]:
#                 c += 1
#                 s[j] = False
#                 if c == K:
#                   a = j
# print(a)