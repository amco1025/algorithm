def bfs(si,sj):
    q = []
    q.append((si,sj))

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                arr[ni][nj] = num
                visited[ni][nj] = 1
                q.append((ni,nj))

N, M, K = map(int, input().split())

arr = [[0]*M for _ in range(N)]
for _ in range(K):
    a,b,c,d  = map(int, input().split())
    si , sj, ei, ej = N-d , a, N-b, c

    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = -1

num = 1
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            arr[i][j] = num
            bfs(i,j)
            num += 1


mx = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] > mx:
            mx = arr[i][j]
li = []
for n in range(1, mx+1):
    a = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == n:
                a += 1
    li.append(a)

print(mx)
li.sort()
print(*li)