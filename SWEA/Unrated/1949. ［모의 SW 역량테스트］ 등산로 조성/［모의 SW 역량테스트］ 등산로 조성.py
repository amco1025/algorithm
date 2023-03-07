dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def dfs(x, y, cut, height):
    global cnt
    global longest
    #  현재 점에서 4방향 탐색
    for d in range(4):
        a, b = x + dx[d], y + dy[d]
        # 4방향 중 간 방향이 범위 안이고 아직 방문하지 않은 곳 이라면
        if not visited[a][b] and 0<=a<n and 0<=b<n:
            # 그리고 그 곳이 현재 위치보다 높이가 낮다면
            if mountain[a][b] < height:
                # 갈 수 있는 곳 +1 갔다고 표시 그 위치에서 다시 dfs
                cnt += 1
                visited[x][y] = True
                dfs(a, b, cut, mountain[a][b])
                # 다음에 다른 방법으로 올 수 있으므로 원래 상태로 돌려놓기
                cnt -= 1
                visited[x][y] = False
                # 간 위치가 현재 보다 높지만 아직 산을 안 잘랐고 잘랐을 때 현재 위치 보다 낮아진다면
            elif not cut and mountain[a][b] - k < height:
                cnt += 1
                visited[x][y] = True
                dfs(a, b, True, height - 1)
                cnt -= 1
                visited[x][y] = False
    if cnt > longest:
        longest = cnt
    return


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    cnt = longest = 1
    mountain = [list(map(int, input().split())) + [100] for _ in range(n)] + [[100] * n]
    highest = max(mountain[i][j] for i in range(n) for j in range(n))
    visited = [[False] * n + [True] for _ in range(n)] + [[True] * n]
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == highest:
                dfs(i, j, False, highest)
    print(f'#{tc}', longest)