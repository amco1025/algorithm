T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    cnt = 1
                    ni = i + di
                    nj = j + dj
                    while 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni = ni + di
                        nj = nj + dj
                    if cnt >= 5:
                        answer = 1


    if answer == 1:
        answer = 'YES'
    else:
        answer = 'NO'

    print("#"+str(tc)+" "+str(answer))