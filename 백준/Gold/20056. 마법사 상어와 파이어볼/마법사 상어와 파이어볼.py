# 배열의 크기와 FIREBALL의 수 이동 횟수
N, M, K = map(int, input().split())
# 파이어볼 저장할 리스트 만들기
fireballs = []
# 파이어볼 입력 받으며 만들어 놓은 리스트에 저장
for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fireballs.append([r-1, c-1, m, s, d])

# 가로, 세로가 N인 배열 만들기
MAP = [[[] for _ in range(N)] for _ in range(N)]

# 방향의 수에 맞추어 dx와 dy 만들기
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# K번 파이어볼 이동
for _ in range(K):
    while fireballs:
        # 파이어볼이 있는 동안 하나씩 꺼내어 이동 방향가 속에 맞추어 새로운 위치를 구한 후 그 위치에 위치, 속력, 방향 저장
        cr, cc, cm, cs, cd = fireballs.pop(0)
        nr = (cr + cs * dx[cd]) % N  # 1번-N번 행 연결되어있기 때문
        nc = (cc + cs * dy[cd]) % N
        MAP[nr][nc].append([cm, cs, cd])

    # 2개 이상인지 체크
    for r in range(N):
        for c in range(N):
            # 2개 이상인 경우 -> 4개의 파이어볼로 쪼개기
            if len(MAP[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])
                while MAP[r][c]:
                    _m, _s, _d = MAP[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:  # 모두 홀수이거나 모두 짝수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m//5:  # 질량 0이면 소멸
                    for d in nd:
                        fireballs.append([r, c, sum_m//5, sum_s//cnt, d])

            # 1개인 경우
            if len(MAP[r][c]) == 1:
                fireballs.append([r, c] + MAP[r][c].pop())

print(sum([f[2] for f in fireballs]))