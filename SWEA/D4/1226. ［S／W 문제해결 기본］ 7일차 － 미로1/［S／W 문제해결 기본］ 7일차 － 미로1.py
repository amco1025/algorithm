def BFS(arr, si, sj): 
    queue = []
    queue.append((si,sj))
    ci, cj = si, sj
    visited[ci][cj] = 1
    while queue:
        ci, cj = queue.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = ci + di
            nj = cj + dj
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj] != 1:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni,nj))
    return visited


T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                si, sj = i, j

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 3:
                ei, ej = i, j

    visited = [[0] * 16 for _ in range(16)]

    answer = BFS(arr, si, sj)
    print("#"+str(tc)+" "+str(answer[ei][ej]))