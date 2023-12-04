n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n+1)
now = [0] * (n + 1)
flag = False

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

for _ in range(k):
    n, a = map(int, input().split())

    if n == 1:
        if indegree[a] != 0:
            flag = True
            break
        else:
            now[a] += 1
            if now[a] == 1:
                for next in graph[a]:
                    indegree[next] -= 1


    else:
        if now[a] <= 0:
            flag = True
            break
        else:
            now[a] -= 1
            if now[a] == 0:
                for next in graph[a]:
                    indegree[next] += 1

if flag:
    print("Lier!")
else:
    print("King-God-Emperor")


