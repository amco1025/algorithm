T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    final = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if li[i][j] == 1:
                if j < N-1:
                    cnt += 1
                else:
                    cnt += 1
                    answer.append(cnt)
            
            elif li[i][j] == 0:
                answer.append(cnt)
                cnt = 0
                
    for p in range(N):
        cnt = 0
        for q in range(N):
            if li[q][p] == 1:
                if q < N -1:
                    cnt += 1
                else:
                    cnt += 1
                    answer.append(cnt)
            elif li[q][p] == 0:
                answer.append(cnt)
                cnt = 0
                
    for k in answer:
        if K == k:
            final += 1
        else:
            continue
    print("#"+str(tc)+" "+str(final))
