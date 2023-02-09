def DFS(v):           # DFS 함수 선언
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            DFS(i)

T  = int(input()) # 테스트 케이스 수 입력

for tc in range(1, T+1): # 테스트 케이스 수 만큼 반복
    n, m = map(int, input().split()) # 사람수와 연결 수

    graph = [[] for _ in range(n + 1)] # 몇 번째 사람이 누구와 연결되어 있는지 보여주는 리스트 생성
    visited = [False] * (n+1) # 아직 방문 안 헀으므로 다 False  입력

    for _ in range(m):        # 연결관계 선언 될 떄마다 그래프 변수에 입력
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    count = 0
    for i in range(1, n+1): # 1 부터 n 까지 넣으며 dfs
        if visited[i] == False:
            count += 1
            DFS(i)

    print("#"+str(tc)+" "+str(count))
