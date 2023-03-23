di = [1, 1, -1, -1]  # 대각선 방향
dj = [1, -1, -1, 1]


def DFS(i, j, k, cnt, eated):
    global sti, stj, maxV, result
    if (i, j) == (sti, stj):  # 출발지점으로 다시 돌아온다면
        result = len(eated)
        if maxV < result:  # 여기서 비교..
            maxV = result
        return

    if i < 0 or i > N - 1 or j < 0 or j > N - 1:  # 범위를 벗어나면 return
        return

    if dessert[i][j] in eated:  # 먹었던 디저트라면 return
        return

    # k=0일 때
    if k == 0:
        DFS(i + 1, j + 1, k, cnt + 1, eated + [dessert[i][j]])
        DFS(i + 1, j - 1, k + 1, cnt + 1, eated + [dessert[i][j]])
    # k=1일 때
    elif k == 1:
        DFS(i + 1, j - 1, k, cnt + 1, eated + [dessert[i][j]])
        DFS(i - 1, j - 1, k + 1, cnt + 1, eated + [dessert[i][j]])
    # k=2일 때
    elif k == 2:
        if i + j == sti + stj:  # 이제 꺾으면 될 때
            DFS(i - 1, j + 1, k + 1, cnt + 1, eated + [dessert[i][j]])
        else:
            DFS(i - 1, j - 1, k, cnt + 1, eated + [dessert[i][j]])
    # k=3일 때
    elif k == 3:
        DFS(i - 1, j + 1, k, cnt + 1, eated + [dessert[i][j]])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]

    maxV = 1
    for sti in range(N):
        for stj in range(N):
            eated = [dessert[sti][stj]]
            result = 1
            DFS(sti + 1, stj + 1, 0, 1, eated)

    if maxV == 1:
        maxV = -1

    print('#{} {}'.format(tc, maxV))