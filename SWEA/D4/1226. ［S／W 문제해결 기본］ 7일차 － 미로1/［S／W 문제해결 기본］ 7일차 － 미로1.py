from collections import deque
 
def bfs(a, b):
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  q = deque()
  q.append([a,b])
  visited[a][b] = 1
 
  while q:
    x,y = q.popleft()
     
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
 
      if 0<=nx<16 and 0<=ny<16:
        if maze[nx][ny] == 3:
          return 1
 
        if maze[nx][ny] == 0 and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append([nx,ny])
   
  return 0
 
 
for tc in range(10):
  n = int(input())
  maze = [list(map(int, input())) for _ in range(16)]
  visited = [[False for _ in range(16)] for _ in range(16)]
  answer = bfs(1, 1)     
  print(f'#{n} {answer}')