from itertools import combinations
import copy
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

candidates = []
virus = []
wall = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            candidates.append((i,j))

        elif arr[i][j] == 2:
            virus.append((i,j))



tmp_walls = combinations(candidates, 3)
ans = 0
for tmp_wall in tmp_walls:
    sm =0
    grid = copy.deepcopy(arr)
    for i, j in tmp_wall:
        grid[i][j] = 1

    now_virus = deque(virus)

    while now_virus:
        x, y = now_virus.popleft()

        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            nx = x + di
            ny = y + dj
            if 0<=nx<N and 0<=ny<M and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                now_virus.append((nx,ny))

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                sm += 1

    ans = max(sm, ans)

print(ans)