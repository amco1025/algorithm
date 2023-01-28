from collections import deque
 
N = int(input())                             # N에 노드의 개수를 입력해 준다.
A = [[] for _ in range(N + 1)]              # 리스트 안에 리스트가 N+1개 있는 리스트를 A에게 할당
for _ in range(N):                          # 변수 값이 중요하지 않아 _ 만 적음 단지 반복문을 0 ~ N-1까지 N번 반복한다.
    Data = list(map(int, input().split()))  # Data 에 특정 노드에서 어떠한 노드에 연결 유무와 연결된 경우 가중치 즉 거리를 할당. 그 값은 사용자가 입력
    index = 0                               # inde 에 0대입
    S = Data[index]                         # S에 Data[index]저장
    index += 1                              # 반복문을 끝내면 index의 값을 1 증가시키고 다시 반복문 N번 채울 때 까지 실행
    while True:                            # True이면 계속하여 반복문 실행
        E = Data[index]                     #
        if E == -1:
            break
        V = Data[index + 1]
        A[S].append((E, V))
        index += 2

distance = [0] * (N + 1)                    # A에는 각 노드들이 가는 노드와 거리 visted는 False가 N+1개 있는 리스트 할당.
visited = [False] * (N + 1)

def BFS(v):                                 # BFS함수 정의
    queue = deque()                         # queue에 deque 할당
    queue.append(v)                         # 노드의 시작점 v를 넣으면 queue에 v추가
    visited[v] = True                      # visted[v]에 True 대입       즉 시작점 v를 추가하면 queue에 v를 추가하고 visted[v]를 True로 변경해준다.
    while queue:                           # queue가 있는 동안 반복
        now_Node = queue.popleft()         # now_Node에서 queue의 값중 가장 먼저 들어온 값을 출력하여 할당해준다. 즉 처음 v값
        for i in A[now_Node]:              # i에다가 A[v]값을 차례대로 넣어주면 반복문 실행
            if not visited[i[0]]:          # visted[i[0]]는 방문 여부 visted[i[1]] 거리 의미 vistedi[0]가 False라면
                visited[i[0]] = True       # visted[i[0]]에 True를 대입하고
                queue.append(i[0])         # queue에 append(i[0])추가 즉 방문 노드 추가
                distance[i[0]] = distance[now_Node] + i[1]  # distance[i[0]]에 거리 추가
BFS(1)
Max = 1
for i in range(2, N + 1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(Max)
distance.sort()
print(distance[N])