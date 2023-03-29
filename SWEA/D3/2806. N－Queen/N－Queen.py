def dfs(i):
    global cnt

    if i == N:
        cnt += 1
        return

    m = 0
    for j in range(N):
        if visited[i][j] == 0:
            m = 1
            break

    if m == 0:
        return

    for j in range(N):
        if visited[i][j] == 0:

            # 가로 세로 방향
            for p in range(N):
                visited[i][p] += 1
                visited[p][j] += 1

            # 대각선 방향
            ci = i
            cj = j

            for di, dj in ((1,1),(1,-1),(-1,1),(-1,-1)):
                for k in range(N):
                    ni = ci + di*k
                    nj = cj + dj*k
                    if 0<=ni<N and 0<=nj<N:
                        visited[ni][nj] += 1

            dfs(i+1)

            for p in range(N):
                visited[i][p] -= 1
                visited[p][j] -= 1

            for di, dj in ((1,1),(1,-1),(-1,1),(-1,-1)):
                for k in range(N):
                    ni = ci + di*k
                    nj = cj + dj*k
                    if 0<=ni<N and 0<=nj<N:
                        visited[ni][nj] -= 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    visited = [[0]*N for _ in range(N)]

    dfs(0)

    print("#"+str(tc)+" "+str(cnt))