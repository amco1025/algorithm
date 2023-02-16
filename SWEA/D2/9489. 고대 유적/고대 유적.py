def dfs(x, y, v, cnt):
    global ans
    if not lst[x][y]: # 만약 0 이라면 
        return
    if m > y + 1 >= 0 == v: # 가로 방향에 1 더한게 범위 내 라면
        if lst[x][y + 1]:
            dfs(x, y + 1, 0, cnt + 1) # 그 값이 1 이라면  cnt에 1 추가후 다시 dfs
    if 0 <= x + 1 < n and v == 1: # 세로 방향에 1 더한게 범위 내라면
        if lst[x + 1][y]: # 그리고 그값이 1 이라면
            dfs(x + 1, y, 1, cnt + 1) # cnt와 세로 방향에 1 추가 후 다시 dfs
    if ans < cnt: # 현재 값 보다 지금이 크다면 변경
        ans = cnt
 
 
t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    cnt, ans = 1, 0
    for i in range(n):
        for j in range(m):
            if lst[i][j]:
                dfs(i, j, 0, cnt)
                dfs(i, j, 1, cnt)
    print(f'#{tc} {ans} ')