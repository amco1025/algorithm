M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bee = [[1]*M for _ in range(M)]

for i in range(N):
    su = arr[i]
    li = []
    cnt = 0
    for i in range(3):
        for j in range(su[i]):
            li.append(cnt)
        cnt+=1
    visited = [[0]*M for _ in range(M)]

    for j in range(0,len(li)//2+1):
        visited[M-1-j][0] = li[j]

    n = len(li)
    li = li[n//2+1:]

    for j in range(1, M):
        visited[0][j] = li[j-1]

    for i in range(1,M):
        for j in range(1,M):
            visited[i][j] = max(visited[i-1][j-1], visited[i][j-1], visited[i-1][j])

    for i in range(M):
        for j in range(M):
                bee[i][j] += visited[i][j]


for i in bee:
    print(*i)
