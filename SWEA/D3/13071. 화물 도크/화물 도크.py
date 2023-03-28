T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [[0]*2 for _ in range(N)]
    #  끝나는 시간이 빠른 순서로 정렬
    for i in range(N):
        s, e = map(int, input().split())
        graph[i][0] = e
        graph[i][1] = s

    graph.sort()
    # 초기 화물 개수 0 시작  -1
    cnt = 0
    end = -1
    # 만약 시작시간이 현재 끝나는 시간보다 크다면 가능한 경우이므로
    for i in range(N):
        # 추가 후 끝나는 시간 변경
        if graph[i][1] >= end:
            end = graph[i][0]
            cnt += 1

    print("#"+str(tc)+" "+str(cnt))
