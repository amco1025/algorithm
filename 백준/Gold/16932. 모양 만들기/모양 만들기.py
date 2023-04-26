
# def dfs():
#     answer = 0
#     visited = [[0]*M for _ in range(N)]
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 1:
#                 q = []
#                 q.append((i,j))
#                 visited[i][j] = 1
#                 sm = 0
#                 while q:
#                     sm += 1
#                     x, y = q.pop(0)
#                     ci = x
#                     cj = y
#                     for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
#                         ni = ci + di
#                         nj = cj + dj
#                         if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
#                             visited[ni][nj] = 1
#                             q.append((ni, nj))
#
#                 answer = max(answer, sm)
#
#     return answer
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# change = []
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             ci = i
#             cj = j
#             for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
#                 ni = ci + di
#                 nj = cj + dj
#                 if 0<=ni<N and 0<=nj<M and [ni,nj] not in change:
#                     change.append((i,j))
#
# ans = -1
# for ch in change:
#     x = ch[0]
#     y = ch[1]
#     arr[x][y] = 1
#     ans = max(dfs(), ans)
#     arr[x][y] = 0
#
# print(ans)

from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * M for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(i, j):
    cnt = 1
    q = deque()
    q.append((i, j))
    visited[i][j] = num
    while q:
        y, x = q.popleft()
        for l in range(4):
            yy = dy[l] + y
            xx = dx[l] + x
            if 0 <= yy < N and 0 <= xx < M:
                if not visited[yy][xx] and graph[yy][xx] == 1:
                    visited[yy][xx] = num
                    q.append((yy, xx))
                    cnt += 1
    return cnt

# '1' 그룹화 진행 -> num은 2부터 시작
num = 2
group = dict()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j)
            group[num] = cnt
            num += 1
# print(group)
# print(visited)

result = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            s = set()
            for l in range(4):
                yy = dy[l] + y
                xx = dx[l] + x
                if 0 <= yy < N and 0 <= xx < M:
                    if graph[yy][xx] == 1 and visited[yy][xx] not in s:
                        s.add(visited[yy][xx])
            res = 1
            # print("test", s)
            for ss in s:
                res += group[ss]
            result = max(result, res)
print(result)