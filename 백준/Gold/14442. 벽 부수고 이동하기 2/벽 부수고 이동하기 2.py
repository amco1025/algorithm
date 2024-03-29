# import sys
# input = sys.stdin.readline
# from collections import deque
# 
# def bfs(x,y):
#     queue = deque()
#     queue.append([x,y,0])
#     visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
#     visited[x][y][0] = 1
#     while queue:
#         x,y,b_cnt = queue.popleft()
#         if x==N-1 and y==M-1:
#             return visited[x][y][b_cnt]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<M:
#                 if not visited[nx][ny][b_cnt]:
#                     if maps[nx][ny]:
#                         if b_cnt < K:
#                             visited[nx][ny][b_cnt+1] = visited[x][y][b_cnt]+1
#                             queue.append([nx,ny,b_cnt+1])
#                         else:
#                             continue
#                     elif not maps[nx][ny]:
#                         visited[nx][ny][b_cnt] = visited[x][y][b_cnt]+1
#                         queue.append([nx,ny,b_cnt])
# 
#     return -1
# 
# N, M, K = map(int, input().split())
# maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# 
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# print(bfs(0,0))

from collections import deque
q = deque()
from sys import stdin
input = stdin.readline

n,m,k = map(int, input().split())
vis = [[[0]*(k+1) for _ in range(m)] for __ in range(n)]
arr = [list(map(int,input().strip())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs() :
    q.append([0,0,k]) # k는 벽을 뚫을 수 있는 수
    vis[0][0][k] = 1
    while q :
        x,y,z = q.popleft()
        if x == n-1 and y == m-1 :
            return vis[x][y][z]
        for i in range(4) :
            nx ,ny = dx[i] + x, dy[i]+y
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny]==1 and z>0 and vis[nx][ny][z-1]==0:
                    vis[nx][ny][z-1] = vis[x][y][z]+1
                    q.append([nx,ny,z-1])
                elif arr[nx][ny]==0 and vis[nx][ny][z]==0:
                    vis[nx][ny][z] = vis[x][y][z]+1
                    q.append([nx,ny,z]) 
    return -1

print(bfs())