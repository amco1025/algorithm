N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
li = list(map(int, input().split()))
cnt = 0

for i in li:
    for j in range(i):
        arr[N-1-j][cnt] = 1
    cnt+=1


for i in range(N-1, -1, -1):
    for j in range(M):
        if arr[i][j] == 0:
            ans = 0

            for k in range(0, j):
                if arr[i][k] == 1:
                    ans += 1
                    break
            for k in range(j, M):
                if arr[i][k] == 1:
                    ans += 1
                    break

            if ans == 2:
                arr[i][j] = -1

ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            ans += 1

print(ans)