def dfs(s):
    stk = []

    while True:
        for e in adj[s]:
            if visited[e] == 0:
                stk.append(s)

                s = e
                visited[s] = 1
                break
        else:
            if stk:
                s = stk.pop()
            else:
                break


T = 10
for tc in range(1, T+1):
    a, b = map(int, input().split())
    li = list(map(int, input().split()))
    adj = [[] for _ in range(100)]

    for i in range(0, 2*b, 2):
        adj[li[i]].append(li[i+1])

    S = 0
    G = 99
    visited = [0] * (100)

    dfs(S)
    print("#"+str(tc)+" "+str(visited[G]))
