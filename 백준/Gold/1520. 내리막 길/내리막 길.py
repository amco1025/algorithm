# import sys
# sys.setrecursionlimit(10 ** 9)
#
# def bfs(si,sj):
#     q = []
#     q.append((si,sj))
#     visited[si][sj] = 1
#      # 현재 위치에서 모든 4방향을 탐색하며 다음에 갈 위치가 현재보다 낮다면 방문 횟수 1 추가
#
#     while q:
#         ci, cj = q.pop(0)
#
#         for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
#             ni = ci + di
#             nj = cj + dj
#
#             if 0<=ni<N and 0<=nj<M and arr[ni][nj] < arr[ci][cj]:
#                 visited[ni][nj] += 1
#                 q.append((ni,nj))
#
#     return visited[N-1][M-1]
#
# N, M = map(int, input().split())
# arr =[list(map(int, input().split())) for _ in range(N)]
#
# visited = [[0]*M for _ in range(N)]
#
# print(bfs(0,0))

import sys
import heapq

def BFS():
    queue = [(-table[0][0],0,0)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        h,x,y = heapq.heappop(queue)
        for dx,dy in direction:
            nx=dx+x
            ny=dy+y
            if 0<=nx<n and 0<=ny<m and table[nx][ny]<table[x][y]:
                if visited[nx][ny] ==0:
                    heapq.heappush(queue,(-table[nx][ny],nx,ny))
                visited[nx][ny] += visited[x][y]
    return visited[n-1][m-1]
input = sys.stdin.readline
n,m = map(int,input().split())
table = [list(map(int,input().split()))for _ in range(n)]
print(BFS())