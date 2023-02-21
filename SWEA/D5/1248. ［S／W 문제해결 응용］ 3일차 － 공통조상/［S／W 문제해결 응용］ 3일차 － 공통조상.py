def BFS_1(v):
    q = [v]
    while q:
        t = q.pop(0)
        if visited_1[t] == 0:
            visited_1[t] = 1
            for i in graph_1[t]:
                if visited_1[i] == 0:
                    q.append(i)
    return visited_1

def BFS_2(v):
    q = [v]
    while q:
        t = q.pop(0)
        if visited_2[t] == 0:
            visited_2[t] = 1
            if visited_1[t] == 1:
                return t
            else:
                for i in graph_1[t]:
                    if visited_2[i] == 0:
                        q.append(i)

def BFS_3(v):
    q = [v]
    while q:
        t = q.pop(0)
        if visited_3[t] == 0:
            visited_3[t] = 1
            for i in graph_2[t]:
                if visited_3[i] == 0:
                    q.append(i)
    return visited_3


T = int(input())

for tc in range(1, T+1):
    N, M, A, B = map(int, input().split())
    li = list(map(int, input().split()))
    graph_1 = [[] for _ in range(N+1)]
    graph_2 = [[] for _ in range(N+1)]
    visited_1 = [0] * (N+1)
    visited_2 = [0] * (N+1)
    visited_3 = [0] * (N+1)
    answer = 0

    for i in range(0, 2*M, 2):
        graph_1[li[i+1]].append(li[i])

    for i in range(0, 2*M, 2):
        graph_2[li[i]].append(li[i+1])

    BFS_1(A)
    answer = BFS_2(B)
    ans = BFS_3(answer)
    final = 0
    for i in ans:
        if i == 1:
            final += 1

    print(f"#{tc} {answer} {final}")
