T = int(input())

def dfs(sm, n, visited):
    global ans

    if n == 11:
        if sum(visited) == 11:
            ans = max(ans, sm)
            return

    for i in range(11):
        if visited[i] == 0:
            if arr[n][i] != 0:
                visited[i] = 1
                dfs(sm+arr[n][i], n+1, visited)
                visited[i] = 0

for _ in range(T):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    ans = 0
    dfs(0,0,visited)

    print(ans)