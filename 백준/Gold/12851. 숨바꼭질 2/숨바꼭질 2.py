from collections import deque

N, K = map(int, input().split())
visit = [[-1,0] for _ in range(100001)] #[걸린시간, 경우의 수]
q = deque()
q.append(N)   #(pos, time)
visit[N][0] = 0
visit[N][1] = 1
while q:
    x = q.popleft()
    for nx in [x-1, x+1, 2*x]:
        if 0<= nx <= 100000:
            # 첫방문이라면
            if visit[nx][0] == -1:
                visit[nx][0] = visit[x][0] + 1
                visit[nx][1] = visit[x][1]
                q.append(nx)
            # 첫방문은 아니지만 최소시간이라면
            elif visit[nx][0] == visit[x][0] + 1:
                visit[nx][1] += visit[x][1]

print(visit[K][0])
print(visit[K][1])