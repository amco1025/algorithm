import collections


def start(h):
    # 채울 물의 양을 0으로 두고 시작
    rtn = 0
    # 모든 배열의 반복문을 돌며 진행
    for i in range(N):
        for j in range(M):
            # 조건에 맞추어 물을 채우기 위해서는 최소 1층의 빌딩이 있어야 한다.
            # 그리고 현재 위치의 빌딩 높이가 반복문의 h보다 작다면
            # 그리고 아직 방문하지 않았다면
            if area[i][j] and area[i][j] < h and not visited[i][j]:
                # rtn의 값을 bfs함수에 따른 값을 더한다.
                rtn += bfs(i, j, h)
    return rtn

def bfs(i, j, h):
    # 현재 반복문에서의 h와 조건을 만족하는 배열의 i,j를 인자로 받아와 bfs함수 실행
    q = collections.deque()
    pos = [[i, j]]
    q.append([i, j])
    visited[i][j] = True
    flag = False
    while q:
        i, j = q.popleft()
        for a in range(4):
            ni, nj = i+di[a], j+dj[a]
            if 0 <= ni < N and 0 <= nj < M and area[ni][nj]!=0:
                if not visited[ni][nj]:
                    if area[ni][nj] < h:
                        visited[ni][nj] = True
                        pos.append([ni, nj])
                        q.append([ni, nj])
            else:
                flag = True

    if flag:
        return 0
    else:
        water = 0
        for i, j in pos:
            area[i][j] += 1
            water += 1
        return water

# 행과 열의 수를 입력
N, M = map(int, input().split())
# 주어진 빌딩의 높이들을 입력
area = [list(map(int, list(input()))) for _ in range(N)]
# 방향을 조정할 수 있는 리스트 생성
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
# 채울 수 있는 물의 양
result = 0

# h에 1부터 9까지 넣으며 반복문 진행
for h in range(1, 10):
    # 각 반복문을 실행할 떄 마다 주어진 배열의 크기만큼 리스트를 만들고 false로 채우고 시작
    visited = [[False] * M for _ in range(N)]
    # result에 만든 함수에 따라 값을 추가
    result += start(h)
print(result)