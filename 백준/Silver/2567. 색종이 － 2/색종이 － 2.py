num = int(input())
arr = [[0] * 101 for _ in range(101)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(num):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

ans = 0

for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            cnt = 0
            for k in range(4):
                ni = i+dx[k]
                nj = j + dy[k]
                if arr[ni][nj] == 1:
                    cnt += 1
            if cnt == 3:
                ans += 1
            if cnt == 2:
                ans += 2
print(ans)