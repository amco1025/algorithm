def DFS(v):
    visited[v] = 0
    for i in graph[v]:
        if visited[i] == 1:
            DFS(i)


N, M = map(int, input().split())
li = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
ans = []
for _ in range(M):
    a = list(map(int, input().split()))
    ans.append(a[1:])
    if a[0] != 0:
        for i in range(len(a)-1):
            for j in range(len(a)-1):
                graph[a[i+1]].append(a[j+1])

for i in range(1,N+1):
    rs = {i}
    graph[i] = [j for j in graph[i] if j not in rs]


for i in range(1, N+1):
    graph[i]  = set(graph[i])
    graph[i] = list(graph[i])

visited = [1] * (N+1)

if li[0] != 0:
    for i in li[1:]:
        DFS(i)

cnt = M

for i in ans:
    for j in i:
        if visited[j] == 0:
            cnt = cnt - 1
            break



print(cnt)
