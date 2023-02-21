def BFS(graph, v, N): # 그래프와, 시작 값, 노드의 개수를 변수
    q = [v] # 시작 값을 큐에 넣는다.
    visited[v] = 1 # 시작점을 방문 했다고 표시
    while q: # 큐에 값이 존재할 떄까지 반복
        t = q.pop(0) # 큐에서 가장 먼저 들어온 값을 pop하여 t에 입력
        for v in graph[t]: # t에서 갈수 있는 노드들을 v에 넣어가며 반복
            if visited[v] == 0: # 만약 v노드를 방문하지 않았다면
                q.append(v) # 큐에 v노드 추가
                visited[v] = visited[t] + 1 # 방문 표시에 전 방문 값 보다 1추가한 값을 넣어준다.
    return visited

T = 10

for tc in range(1, T+1):
    A, B = map(int, input().split())
    li = list(map(int, input().split()))
    mx = max(li) # 노드의 개수는 리스트에 있는 값 중 가장 큰 값
    graph = [[] for _ in range(mx+1)]
    visited =[0] * (mx+1)

    for i in range(0, len(li), 2): # 그래프 만들기 , 중복 x
        if li[i+1] not in graph[li[i]]:
            graph[li[i]].append(li[i+1])

    answer = BFS(graph, B, mx)

    ans = [(i, answer[i]) for i in range(mx+1)] # ans리스트에 노드의 번호와 그 노드가 몇번만에 방문 되었는지 표시
    final = 0 # 여태 까지 나온 방문 값중 가장 큰 값 나타내줄 변수
    sol = 0 # 그 변수의 인덱스 저장

    for i in range(len(ans)): # 만약 몇 번째로 방문 했는지 보여주는 값이 전 노드들 보다 크다면 sol에 그 리스트 입력 final에 몇 번째로 방문 되었는지 입ㄹ겨
        if ans[i][1] >= final:
            sol = i
            final = ans[i][1]

    print("#"+str(tc)+" "+str(sol))