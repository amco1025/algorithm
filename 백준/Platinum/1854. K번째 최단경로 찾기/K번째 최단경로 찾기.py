import sys
import heapq
input = sys.stdin.readline
N, M, K = map(int, input().split())   # 노드 개수, 에지 개수 , 몇 번쨰 최단거리로 할건지 입력
W = [[] for _ in range(N+1)]         # W 에 인접 리스트 저장 연결된 노드와 가중치 같이 입력
distance = [[sys.maxsize] * K for _ in range(N+1)] # 만약 k가 3이라고 한다면 3번째 최단거리까지 알아야 하므로 노드 개수 당 k개의 리스트를 같는 distance리스트 생성

for _ in range(M):      # 인접 리스트 만들기
    a, b, c = map(int, input().split())
    W[a].append((b,c))

pq = [(0,1)]   # 시작 노드가 무조건 1이라고 문제에서 주어졌으므로 pq에 [(0,1)] 할당
distance[1][0] = 0  # distance[1][0]에 0 할당 시작노드가 1이므로 1부터 1까지 거리는 0이기 때문에
while pq:
    cost,node = heapq.heappop(pq)   # 가중치와 노드에 heapq.heappop(pq)대입
    for nNode, nCost in W[node]:
        sCost = cost + nCost
        if distance[nNode][K-1] > sCost:
            distance[nNode][K-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, [sCost, nNode])

for i in range(1,N+1):
    if distance[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K-1])