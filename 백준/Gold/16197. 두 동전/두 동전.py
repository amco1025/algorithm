import sys

sys.setrecursionlimit(10000)


def game(start, sm):
    global ans
    # 현재 ans보다 sm이 크면 끝
    if sm > 10:
        return

    if sm >= ans:
        return

    if arr[start[0][0]][start[0][1]] == -1 and arr[start[1][0]][start[1][1]] == -1:
        return

    # 1나만 살면 저장
    if (arr[start[0][0]][start[0][1]] == -1 and arr[start[1][0]][start[1][1]] != -1) or (arr[start[0][0]][start[0][1]] != -1 and arr[start[1][0]][start[1][1]] == -1):
        ans = min(sm, ans)

    else:
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
            x = 0
            y = 0

            nx = start[0][0] + di
            ny = start[0][1] + dj
            ni = start[1][0] + di
            nj = start[1][1] + dj

            if arr[nx][ny] != '#':
                start[0][0] = nx
                start[0][1] = ny
                x = 1

            if arr[ni][nj] != '#':
                start[1][0] = ni
                start[1][1] = nj
                y = 1

            game(start, sm+1)

            if x == 1:
                start[0][0] -= di
                start[0][1] -= dj

            if y == 1:
                start[1][0] -= di
                start[1][1] -= dj


n, m = map(int, input().split())
arr = [[-1] * (m + 2)]

# 입력 받으면서 좌우측에 -1로 패딩
for _ in range(n):
    row = list(input())
    arr.append([-1] + row + [-1])

# 하단 패딩 추가
arr.append([-1] * (m + 2))

start = []

for i in range(n+2):
    for j in range(m+2):
        if arr[i][j] == 'o':
            start.append([i,j])

ans = 11

game(start, 0)

if ans > 10:
    print(-1)
else:
    print(ans)