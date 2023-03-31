def bfs(si,sj,n):
    q = []
    q.append((si,sj))
    a = arr[si][sj]
    visited[si][sj] = 1
    while q:
        n+=1
        ci, cj = q.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == a:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni,nj))
    return n

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 이동방향 동=1 서=2 남=3 북=4
dir = 1
cnt = 0
# 현재 주사위
li = [6,1,5,2,3,4]
si = 0
sj = 0

for _ in range(K):
    x = 0
    visited = [[0] * M for _ in range(N)]
    if dir == 1 and x == 0:
        if sj < M-1:
            # 현재 위치 바꾸기
            sj += 1
            # 주사위 상태 바꾸기
            li[0], li[1], li[4], li[5] = li[4], li[5], li[1], li[0]
            # 이동 방향 바꾸기
            if li[0] > arr[si][sj]:
                dir = 3
            if li[0] < arr[si][sj]:
                dir = 4
            # 그 곳에서의 점수 구하기
            cnt += bfs(si,sj,0) * arr[si][sj]
            x += 1
        else:
            dir = 2
            sj -= 1
            li[0], li[1], li[4], li[5] = li[5], li[4], li[0], li[1]
            if li[0] > arr[si][sj]:
                dir = 4
            if li[0] < arr[si][sj]:
                dir = 3
            cnt += bfs(si, sj, 0) * arr[si][sj]
            x += 1
            # 점수 더하기
    if dir == 2 and x == 0:
        if sj > 0:
            sj -= 1
            li[0], li[1], li[4], li[5] = li[5], li[4], li[0], li[1]
            if li[0] > arr[si][sj]:
                dir = 4
            if li[0] < arr[si][sj]:
                dir = 3
            cnt += bfs(si, sj, 0) * arr[si][sj]
            x += 1
        else:
            dir = 1
            sj += 1
            li[0], li[1], li[4], li[5] = li[4], li[5], li[1], li[0]
            if li[0] > arr[si][sj]:
                dir = 3
            if li[0] < arr[si][sj]:
                dir = 4
            cnt += bfs(si, sj, 0) * arr[si][sj]
            x += 1
    if dir == 3 and x == 0:
        if si < N-1:
            si += 1
            li[0], li[1], li[2], li[3] = li[2], li[3], li[1], li[0]
            if li[0] > arr[si][sj]:
                dir = 2
            if li[0] < arr[si][sj]:
                dir = 1
            cnt += bfs(si,sj,0) * arr[si][sj]
            x += 1
        else:
            dir = 4
            si -= 1
            li[0], li[1], li[2], li[3] = li[3], li[2], li[0], li[1]
            if li[0] > arr[si][sj]:
                dir = 1
            if li[0] < arr[si][sj]:
                dir = 2
            cnt += bfs(si, sj,0) * arr[si][sj]
            x += 1
    if dir == 4 and x == 0:
        if si > 0:
            si -= 1
            li[0], li[1], li[2], li[3] = li[3], li[2], li[0], li[1]
            if li[0] > arr[si][sj]:
                dir = 1
            if li[0] < arr[si][sj]:
                dir = 2
            cnt += bfs(si, sj, 0) * arr[si][sj]
            x += 1
        else:
            dir = 3
            si += 1
            li[0], li[1], li[2], li[3] = li[2], li[3], li[1], li[0]
            if li[0] > arr[si][sj]:
                dir = 2
            if li[0] < arr[si][sj]:
                dir = 1
            cnt += bfs(si, sj, 0) * arr[si][sj]
            x += 1

print(cnt)