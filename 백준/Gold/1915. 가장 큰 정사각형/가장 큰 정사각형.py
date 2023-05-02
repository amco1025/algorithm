# n, m = map(int, input().split())
# 
# arr = [list(map(int, input())) for _ in range(n)]
# ans = 0
# 
# for i in range(n):
#     for j in range(m):
#         if ans > (n-i)*(m-j):
#             break
# 
#         if arr[i][j] == 1:
#             N = 0
#             while arr[i+N][j] == 1 and arr[i][j+N] and i+N < n-1 and j+N < m-1:
#                 N += 1
# 
#             sm = 0
# 
#             for p in range(i, i+N):
#                 for q in range(j, j+N):
#                     if arr[p][q] == 1:
#                         sm += 1
# 
#             if sm == N*N:
#                 ans = max(sm, ans)
# 
# print(ans)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
dp = [[0] * m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(dp[i][j], answer)

print(answer * answer)