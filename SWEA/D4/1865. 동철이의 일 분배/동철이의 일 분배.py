T = int(input())

def dfs(i, sm):
    global ans

    # 가지 치기
    if sm <= ans:
        return

    # 종료 조건
    if i == N:
        ans = max(sm, ans)
        return

    # 하부 조건
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(i+1, sm*arr[i][j]*0.01)
            visited[j] = 0


for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = -1
    dfs(0, 1)

    print("#%d %f" % (tc, ans * 100))