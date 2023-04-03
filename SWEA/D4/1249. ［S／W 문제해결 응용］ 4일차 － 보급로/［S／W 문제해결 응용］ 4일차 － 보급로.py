def bfs(si, sj):
    # 큐에 시작위치 저장
    q = []
    q.append((si, sj))
    
    # 큐가 있는동안 반복문 진행
    while q:
        # 가장 먼저 저장된 값 꺼내서 현재 위치에 저장
        x, y = q.pop(0)
        ci = x
        cj = y
        # 4방향을 돌며 범위 안에 있고 여태까지 최소로 간 시간보다 현재 방법으로 간 시간이 작다면 변경 후 현재 위치 큐에 저장
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] > visited[ci][cj] + arr[ni][nj]:
                    visited[ni][nj] = visited[ci][cj] + arr[ni][nj]
                    q.append((ni,nj))

    return visited[N-1][N-1]

T = int(input())

# 각 길의 상태를 저장할 리스트 생성
# 여러 방법으로 특정 지점에 도달할 때 최소의 시간을 저장할 리스트 생성
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[1000000]*N for _ in range(N)]
    visited[0][0] = 0
    ans = bfs(0,0)
    print("#"+str(tc)+" "+str(ans))