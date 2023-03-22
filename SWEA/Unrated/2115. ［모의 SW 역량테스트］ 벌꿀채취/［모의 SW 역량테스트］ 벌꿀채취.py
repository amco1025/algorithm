import itertools

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] * arr[i][j]

    mx = 0
    for i in range(0,N):
        for j in range(0,N):
            ans = []
            for k in range(M):
                if j+k < N:
                    ans.append(arr[i][j+k])
            for t in range(1, C+1):
                nCr = itertools.combinations(ans,t)
                for h in nCr:
                    h = list(h)
                    if sum(h) >mx:
                        a = 0
                        for p in h:
                            a += p**(1/2)
                        if a <= C:
                            x = i
                            y = j
                            mx = sum(h)
    for k in range(M):
        arr[x][y+k] = 0

    mx_1 = 0
    for i in range(0,N):
        for j in range(0,N):
            ans = []
            for k in range(M):
                if j+k < N:
                    ans.append(arr[i][j+k])
            for t in range(1, C+1):
                nCr = itertools.combinations(ans,t)
                for h in nCr:
                    h = list(h)
                    if sum(h) > mx_1 and x != i:
                        a = 0
                        for p in h:
                            a += p**(1/2)
                        if a <= C:
                            mx_1 = sum(h)
    ans = mx+mx_1

    print("#"+str(tc)+" "+str(ans))