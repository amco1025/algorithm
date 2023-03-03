T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(M):
            n = arr[i][j]
            cnt = 0
            for k in range(1,n+1):
                for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                    ni = i + di * k
                    nj = j + dj * k
                    if 0<=ni<N and 0<=nj<M:
                        cnt += arr[ni][nj]
            cnt += arr[i][j]
            if cnt > mx:
                mx = cnt

    print("#"+str(tc)+" "+str(mx))