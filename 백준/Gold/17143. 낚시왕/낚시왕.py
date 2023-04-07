R, C, M = map(int, input().split())
sharks = dict()
res = 0
fisherman = -1

for _ in range(M):
    # 위치/ 속력/ 방향/ 크기
    # 키 값/  나머지 value
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1,c-1)] = [s,d,z]

    # 방향 1 : 위, 2 : 아래, 3: 오른쪽, 4: 왼쪽
    # 현재 낚시와 위치

for _ in range(C):
    # 1. 낚시왕이 이동
    fisherman += 1
    # 2. 가장 가가운 상어 잡기
    for i in range(R):
        if (i, fisherman) in sharks:
            shark = sharks[(i, fisherman)]
            res += shark[2]
    # 2.a 상어 사라짐
            del sharks[(i,fisherman)]
            break
    # 3. 상어 이동
    next_sharks = dict()
    # 여기다가 이동 시킬 예정
    for key, value in sharks.items():
        x, y = key
        s, d, z = value
        m = s
        # 만약 방향위 위 아래
        if d == 1 or d == 2:
            s = s % (R * 2 - 2)
        else:
            s = s % (C * 2 - 2)

        while s:
            if d == 4:
                if y > s:
                    y = y - s
                    s = 0

                else:
                    s = s - y
                    y = 0
                    d = 3

            elif d == 3:
                if C - y -1 > s:
                    y = y + s
                    s = 0

                else:
                    s = s - (C-y-1)
                    y = C - 1
                    d = 4

            elif d == 1:
                if x > s:
                    x = x - s
                    s = 0

                else:
                    s = s - x
                    x = 0
                    d = 2

            elif d == 2:
                if R - x -1 > s:
                    x = x + s
                    s= 0

                else:
                    s = s - (R-x-1)
                    x = R - 1
                    d = 1
        if (x, y) in next_sharks:
            shark_now = next_sharks[(x, y)]
            n = shark_now[2]
            if z > n:
                next_sharks[(x,y)] = [m,d,z]
        else:
            next_sharks[(x,y)] = [m,d,z]

    sharks = next_sharks
# 4. 큰 상어가 나머지 상어 먹기

print(res)
# res . 낚시왕이 잡은 상어
