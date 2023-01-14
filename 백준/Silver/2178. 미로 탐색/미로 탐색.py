import sys
from collections import deque

input = sys.stdin.readline
del input

N, M = map(int, input().split())

graph = [] 

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    queue = deque()
    queue.append([a, b])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]  # 행값
            ny = y + dy[i]  # 열값

            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    return graph[N - 1][M - 1]


print(bfs(0, 0))