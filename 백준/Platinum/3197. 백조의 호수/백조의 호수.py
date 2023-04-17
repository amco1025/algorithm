
# import sys
# input = sys.stdin.readline
# from collections import deque
#
# def melt():
#     ice = [[0]*M for _ in range(N)]
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'X':
#                 ci = i
#                 cj = j
#                 for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
#                     ni = ci + di
#                     nj = cj + dj
#                     if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '.':
#                         ice[ci][cj] = 1
#                         break
#
#     for i in range(N):
#         for j in range(M):
#             if ice[i][j] == 1:
#                 arr[i][j] = '.'
#
# # 갈 수 있는 곳 돌며 표시
# def bfs(si,sj,visited):
#     visit = [[0]*M for _ in range(N)]
#     q = deque()
#     q.append((si,sj))
#
#     while q:
#         x, y = q.popleft()
#         ci = x
#         cj = y
#         for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
#             ni = ci + di
#             nj = cj + dj
#             if 0<=ni<N and 0<=nj<M and visit[ni][nj] == 0 and (arr[ni][nj] == '.' or arr[ni][nj]=='L'):
#                 visit[ni][nj] = 1
#                 q.append((ni,nj))
#
#     for i in range(N):
#         for j in range(M):
#             if visit[i][j] == 1:
#                 visited[i][j] = 1
#
# N, M = map(int, input().split())
#
# arr = [list(map(str, input())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# n = 0
# ans = 0
#
# # 시작점과 도착점 si,sj ei,ej 에 저장
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'L' and n == 0:
#             si = i
#             sj = j
#             n += 1
#         elif arr[i][j] == 'L' and n ==1:
#             ei = i
#             ej = j
#
# # si sj를 시작점으로하여 bfs 실행
# bfs(si, sj, visited)
#
# while visited[ei][ej] != 1:
#     ans+=1
#     melt()
#     bfs(si,sj,visited)
#
# print(ans)

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while wq:
        x, y = wq.popleft()
        if a[x][y] == 'X':
            a[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not wc[nx][ny]:
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
wc = [[0]*n for _ in range(m)]

a, swan = [], []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'L':
            swan.extend([i, j])
            wq.append([i, j])
        elif a[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1])
a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1