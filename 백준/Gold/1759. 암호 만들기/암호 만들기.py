def dfs(i, n, ans, j, m):
    global answer

    if n == N:
        if m >= 1 and j >= 2:
            answer.append(ans)
        return

    if i > M-1:
        return


    if li[i] in ['a', 'e', 'i', 'o', 'u']:
        dfs(i+1, n+1, ans+li[i], j, m+1)
        dfs(i+1, n, ans, j, m)
    else:
        dfs(i + 1, n + 1, ans + li[i], j+1, m)
        dfs(i + 1, n, ans, j, m)


N, M = map(int, input().split())
li = list(map(str, input().split()))
li.sort()
answer = []
dfs(0, 0, '', 0, 0)

for i in answer:
    print(i)