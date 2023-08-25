R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            sm = 0
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni = i + di
                nj = j + dj
                if 0<=ni<R and 0<=nj<C and arr[ni][nj] == '.':
                    sm += 1
                elif ni<0 or ni>=R or nj<0 or nj>=C:
                    sm += 1
            if sm >= 3:
                visited[i][j] = 1


for i in range(R):
    for j in range(C):
        if visited[i][j] == 1:
            arr[i][j] = '.'

min_r = 10000
mx_r = 0
min_c = 10000
mx_c = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            min_r = min(min_r, i)
            min_c = min(min_c, j)
            mx_r = max(mx_r, i)
            mx_c = max(mx_c, j)

for i in range(min_r, mx_r+1):
    for j in range(min_c, mx_c+1):
        print(arr[i][j], end="")
    print()


