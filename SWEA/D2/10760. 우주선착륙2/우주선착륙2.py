T = int(input())

for tc in range(1, T+1): # 문제에 주어진 리스트 입력
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0 # 주변에 자신보다 낮은 위치가 4개 이상인 곳

    for i in range(N): # 모든 점에서 시작
        for j in range(M):
            cnt = 0 # 자기 주변의 자신보다 낮은 곳
            for di,dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)): # 8방향 탐색
                ni, nj = i + di , j +dj # 새로운 좌표
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] < arr[i][j]: #조건 만족한다면
                    cnt += 1 # 자신보다 낮은곳에 1추가
            if cnt >= 4: # 그 값이 3보다 크다면
                answer += 1 # 출력 값에 1 추가

    print("#"+str(tc)+" "+str(answer))