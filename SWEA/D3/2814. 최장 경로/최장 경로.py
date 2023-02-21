# def BFS(graph, v, N):
#     visited = [0] * (N + 1)
#     q = [v]
#     visited[v] = 1
#     while q:
#         t = q.pop(0)
#         for i in graph[t]:
#             if visited[i] == 0:
#                 q.append(i)
#                 visited[i] = visited[t] + 1
# 
#     return visited
# 
# T = int(input())
# 
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     graph = [[] for _ in range(N+1)]
#     answer = []
# 
#     for _ in range(M):
#         a, b = map(int, input().split())
#         if b not in graph[a]:
#             graph[a].append(b)
#             graph[b].append(a)
# 
#     for i in range(1, N+1):
#         answer.append(BFS(graph, i, N))
# 
#     ans = 0
# 
#     for i in answer:
#         for j in i:
#             if j > ans:
#                 ans = j
# 
#     print("#"+str(tc)+" "+str(ans))


def dfs(idx, cnt):
    global max
    visit[idx] = True
    if cnt > max:
        max = cnt
    for i in s[idx]:
        if not visit[i]:
            dfs(i, cnt + 1)
            visit[i] = 0


for tc in range(int(input())):
    n, m = map(int, input().split())
    s = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        s[x].append(y)
        s[y].append(x)
    max = 0

    for i in range(1, n + 1):
        visit = [0] * (n + 1)
        dfs(i, 1)
    print('#%d %d' % (tc + 1, max))
    
# bfs로 다시 풀어보기
