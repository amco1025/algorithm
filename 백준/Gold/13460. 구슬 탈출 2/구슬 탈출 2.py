from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입출력 위한 코드

# 보드의 가로와 세로 크기 입력
n, m = map(int, input().split())
graph = []
# 주어진 보드 입력
# 처음 빨간 구슬의 위치와 파란 구슬의 위치를 저장
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':  # 빨간구슬 위치
            rx, ry = i, j
        elif graph[i][j] == 'B':  # 파란구슬 위치
            bx, by = i, j

# 상 하 좌 우로 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 처음 빨간 구슬과 파란 구슬를 인수로 하여 bfs 함수 진행
def bfs(rx, ry, bx, by):
    # q에 deque 선언
    q = deque()
    # q에 빨간 구슬과 파란 구슬의 위치 입력하기
    q.append((rx, ry, bx, by))
    # 방문여부를 판단하기 위한 리스트
    visited = []
    # 방문한 곳인지를 확인하기 위하여 현재 빨간 구슬과 파란 구슬의 위치 저장하기
    visited.append((rx, ry, bx, by))
    # 움직인 횟수
    count = 0
    # q가 있는 동안 반복문 진행
    while q:
        # q의 길이만큼 반복문 진행
        for _ in range(len(q)):
            # q에 있는 빨간 구슬과 파란 구슬의 위치를 rx,ry,bx,by에 저장
            rx, ry, bx, by = q.popleft()
            # 움직인 횟수가 10회 초과면 -1 출력
            if count > 10:
                print(-1)
                return
            # 현재 빨간 구슬의 위치가 구멍이라면 count출력
            if graph[rx][ry] == 'O':
                print(count)
                return
            # 옮길 빨간 구슬의 위치를 저장하기 위해 nrx,nry 만들기
            for i in range(4):  # 4방향 탐색
                nrx, nry = rx, ry
                # #일 때까지 혹은 구멍일 때까지 움직임
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    # 도착한 곳이 구멍이라면 break
                    if graph[nrx][nry] == 'O':
                        break
                # 빨간 구슬과 마찬가지로 파란 구슬도 진행
                nbx, nby = bx, by
                while True:  # #일 때까지 혹은 구멍일 때까지 움직임
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == '#':  # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == 'O':
                        break
                # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                if graph[nbx][nby] == 'O':
                    continue
                # 두 구슬의 위치가 같다면
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):  # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:  # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)  # 10회가 초과하지 않았지만 10회 내에도 구멍에 들어가지 못하는 경우

bfs(rx, ry, bx, by)