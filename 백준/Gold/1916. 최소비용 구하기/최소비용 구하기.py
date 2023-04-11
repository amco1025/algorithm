def dijkstra(s, e):
    q = PriorityQueue()
    # 우선순위 큐에 시작 노드 저장
    q.put((0, s))
    # 시작점의 거리는 0
    dist[s] = 0
    
    # 큐가 있는동안 반복문 진행
    while q.qsize() > 0:
        # nowNode의 변수의 현재 노드와 거리
        nowNode = q.get()
        # now에 현재 노드
        now = nowNode[1]
        # 방문 했다고 표시
        if not visit[now]:
            visit[now] = 1
            # 연결된 것돌을 넣으며 만약 그 곳이 아직 방문되지 않았고 현재 거리보다 지금 거리에서 거기 가는 거리더한것 보다 크다면
            for n in myList[now]:
                if not visit[n[0]] and dist[n[0]] > dist[now] + n[1]:
                    # 거리 정보 변경후 q에 지금 방문한 노드 추가
                    dist[n[0]] = dist[now] + n[1]
                    q.put((dist[n[0]], n[0]))
    return dist[e]


import sys
from queue import PriorityQueue
input = sys.stdin.readline

# 노드의 수와 에지의 수 입력
N = int(input())
M = int(input())
# 그래프 만들고 거리 모두 무한으로 초기화
myList = [[] for _ in range(N+1)]
dist = [sys.maxsize] * (N+1)
visit = [0]*(N+1)

# 그래프 만들기
for _ in range(M):
    s, e, w = map(int, input().split())
    myList[s].append((e,w))

# 시작노드와 종료 노드 입력
si, ei = map(int, input().split())

print(dijkstra(si,ei))
