def BFS(arr, i, j):
    global ans
    q = []
    q.append([i,j])
    while q:
        ci, cj = q.pop(0)
        if visited[ci][cj] == 0:
            visited[ci][cj] = 1
            ans += 1
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni = ci + di
                nj = cj + dj
                if 0<=ni<N and 0<=nj<N and visited[ni][nj] != 1 and arr[ci][cj] == arr[ni][nj] - 1:
                    q.append((ni,nj))
    return ans



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(N):
            ans = 0
            visited = [[0]*N for _ in range(N)]
            BFS(arr, i, j)
            if ans > mx:
                answer = []
                mx = ans
                answer.append(arr[i][j])
                answer.append(ans)
            elif ans == mx:
                if answer[0] > arr[i][j]:
                    answer[0] = arr[i][j]

    print(f'#{tc}', *answer)