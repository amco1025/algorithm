def bfs(si,sj):
    # q에 deque 형식으로 현재의 상어 위치와 0 할당
    q = collections.deque([(si,sj,0)])

    dist_list = []
    visited = [[False]*n for _ in range(n)]
    visited[si][sj] = True
    min_dist = int(500)
    while q:
        # 현재위치와 거리를 나타내주는 변수를 만들고 값 할당
        ci,cj,dist = q.popleft()
        # 4방향 탐색
        for i in range(4):
            ni = dx[i]+ci
            nj = dy[i]+cj
            # 4방향을 보며 그 곳이 범위 안이고 아직 방문하지 않았다면
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj]:
                # 그 곳이 갈 수 있는 곳이라면
                if arr[ni][nj] <= size:
                    # 방문 했다고 표시
                    visited[ni][nj] = True
                    # 먹을 수 있는 물고기 라면
                    if 0<arr[ni][nj]<size:
                        # min_dist에 현재 시간을 넣고
                        min_dist = dist
                        # 먹을 수 있는 물고기 리스트에 가는데 걸리는 시간 행 열 위치 순으로 입력
                        dist_list.append((dist+1,ni,nj))
                    # 먹을 수 있는 물고기가 아니라면
                    # 전에 저장되어 있는 물고기를 먹는 시간보다 빨리 먹거나 같은 시간에 먹을 가능성이 있다면
                    if dist+1 <= min_dist:
                        q.append((ni,nj,dist+1))
    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False

import sys,collections
# 현재 상어의 크기
size = 2
# 먹은 물고기의 수 만약 먹은 물고기의 수가 자신의 크기와 같아져 크기가 증가하면 초기화
eat = 0
# 물고기의 수
fish_cnt = 0
# 물고기의 위치
fish_pos = []
# 엄마 상어에게 도움을 요청할 떄까지의 시간
time = 0
dx = (0,0,1,-1)
dy = (1,-1,0,0)

n = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 배열 전체를 돌며 물고기의 수와 물고기가 있는 위치 상어가 있는 위치를 각 변수에 저장
for i in range(n):
    for j in range(n):
        if 0 < arr[i][j] <=6:
            fish_cnt +=1
            fish_pos.append((i,j))
        elif arr[i][j] == 9:
            si = i
            sj = j
# 상어가 있는 위치의 값을 0으로 변경
arr[si][sj] = 0

# 물고기가 있는 동안 반복문 진행
while fish_cnt :
    result = bfs(si,sj)
    if not result:
        break
    si,sj = result[1],result[2]
    time +=result[0]
    eat += 1
    fish_cnt -= 1
    if size == eat:
        size +=1
        eat =0
    arr[si][sj] = 0

print(time)
