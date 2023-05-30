from collections import deque

# n : 밭의 크기 m : 초기 나무의 수 k : 년도
n, m, k = map(int, input().split(' '))

# 겨울에 추가할 각 배열의 양분의 양
a = [list(map(int, input().split(' '))) for _ in range(n)]

# 현재 양분의 양 초기에 모든 칸 5로 고정
graph = [[5] * n for _ in range(n)]

# 각 칸의 나무 나이가 적은 순으로 양분을 먹기 떄문에 deque사용
trees = [[deque() for _ in range(n)] for _ in range(n)]

# 죽은나무 저장할 리스트
dead_trees = [[list() for _ in range(n)] for _ in range(n)]

# 처음에 주어진 나무들을 나무의 리스트에 할당
for _ in range(m):
    x, y, z = map(int, input().split(' '))
    trees[x - 1][y - 1].append(z)


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 봄과 여름에 일어나는 일
def spring_summer():
    for i in range(n):
        for j in range(n):
            # 나무가 심어진 배열을 돌면서 각 칸의 현재 나무의 수를 변수에 저장
            len_ = len(trees[i][j])
            # 그 수만큼 반복
            for k in range(len_):
                # 현재 그 칸의 양분이 나무의 다이보다 적다면
                if graph[i][j] < trees[i][j][k]:
                    # 그 현재 나무부터 그 칸 끝 나무까지 죽은 나무 리스트에 저장
                    for _ in range(k, len_):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                else:
                    # 그렇지 않다면 양분을 나무의 나이 만큼 감소 시키고 나무 나이 1 증가
                    graph[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    # 죽은나무들의 나이의 반 만큼을 양분으로 변환하여 양분 추가
    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                graph[i][j] += dead_trees[i][j].pop() // 2

# 가을과 겨울에 일어나는 일
def fall_winter():
    for i in range(n):
        for j in range(n):
            # 배열을 돌며 나무의 나이가 5의 배수인 나무가 있다면
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    # 인접한 8칸에 나이가 1인 나무 추가
                    for l in range(8):
                        nx, ny, = i + dx[l], j + dy[l]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[nx][ny].appendleft(1)
            # 각 칸에 처음 주어진 각 칸의 양분 추가
            graph[i][j] += a[i][j]


for i in range(k):
    spring_summer()
    fall_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)