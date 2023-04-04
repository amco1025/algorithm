T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    virus = [list(map(int, input().split())) for _ in range(K)]
    # 주어진 시간 만큼 반복
    for _ in range(M):

        # 각 바이러스에 대하여 조건에 맞추어 진행
        for i in range(len(virus)):
            # 각 바이러스가 가진 방향에 맞추어 현재 위치를 바꿈
            if virus[i][3] == 1:
                virus[i][0] -= 1
            elif virus[i][3] == 2:
                virus[i][0] += 1
            elif virus[i][3] == 3:
                virus[i][1] -= 1
            elif virus[i][3] == 4:
                virus[i][1] += 1

            # 바이러스가 경계에 갔다면 방향을 반대로 바꾸고 가진 바이러스의 수를 반으로 줄임
            if virus[i][0] == 0 or virus[i][1] == 0 or virus[i][0] == N - 1 or virus[i][1] == N - 1:
                virus[i][2] = virus[i][2] // 2

                if virus[i][3] == 1:
                    virus[i][3] = 2
                elif virus[i][3] == 2:
                    virus[i][3] = 1
                elif virus[i][3] == 3:
                    virus[i][3] = 4
                elif virus[i][3] == 4:
                    virus[i][3] = 3


        # i 좌표 j 좌표 가진 바이러스 순으로 정렬
        virus.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
        i = 1
        # 만약 전 바이러스와 좌표가 같으면 현재 가지고 있는 바이러스를 전 바이러스 군집에 주고 삭제
        while i < len(virus):

            if virus[i-1][:2] == virus[i][:2]:
                virus[i-1][2] += virus[i][2]
                virus.pop(i)

            else:
                i+=1

    ans = 0
    for i in virus:
        ans += i[2]

    print("#"+str(tc)+" "+str(ans))