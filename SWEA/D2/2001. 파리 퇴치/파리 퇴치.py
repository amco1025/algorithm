T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            sm = 0
            for p in range(M):
                for q in range(M):
                    if arr[i+p][j+q] > 30:
                        arr[i+p][j+q] = 30
                    sm += arr[i+p][j+q]
            answer.append(sm)


    print("#"+str(tc)+" "+str(max(answer)))