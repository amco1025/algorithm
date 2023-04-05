def bfs_1(si,sj,cnt):
    q = []
    q.append((si,sj, cnt))
    visited[si][sj] = 1

    while q:
        ci, cj, n = q.pop(0)

        if n > T:
            break

        if ci == N-1 and cj == M-1:
            break

        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni,nj,n+1))

def bfs_2(si,sj,cnt):
    q = []
    q.append((si,sj, cnt))
    visited_1[si][sj] = 1

    while q:
        ci, cj, n = q.pop(0)

        if n > T:
            break

        if arr[ci][cj] == 2:
            visited_1[N-1][M-1] = visited_1[ci][cj] + N + M - ci - cj - 2
            break

        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<M and visited_1[ni][nj] == 0 and arr[ni][nj] != 1:
                visited_1[ni][nj] = visited_1[ci][cj] + 1
                q.append((ni,nj,n+1))

N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited_1 = [[0]*M for _ in range(N)]
bfs_1(0,0,0)
bfs_2(0,0,0)
ans_1 = visited[N-1][M-1] - 1
ans_2 = visited_1[N-1][M-1] - 1

if ans_1 == -1:
    ans_1 = 100000

if ans_2 == -1:
    ans_2 = 100000

ans = min(ans_1, ans_2)

if ans > T:
    print('Fail')
else:
    print(ans)