def bfs(i, j):
    visited[i][j] = 1
    q = []
    q.append((i,j))

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                visited[ni][nj] = 1
                q.append((ni,nj))

while True:
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    if m == 0 and n == 0:
        break
    visited = [[0]*m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                ans += 1

    print(ans)