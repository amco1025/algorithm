# 배열의 크기와 처음 주사위를 놓는 좌표 마지막으로 명령의 개수 입력
N, M, X, Y, K = map(int, input().split())
# 보드의 상황 입력
arr = [list(map(int, input().split())) for _ in range(N)]
# 명령의 방향 입력 동쪽=1 서쪽=2, 북쪽=3, 남쪽=4
li = list(map(int, input().split()))

# 위, 아래, 앞, 뒤, 오, 왼
dice = [0,0,0,0,0,0]
ans = []
# 명령을 넣으며 각 방향에 맞추어 조건문 진행
for i in li:
    # 동쪽이라면
    if i == 1:
        # 동쪽으로 한칸 움직여도 보드 밖을 벗어나지 않는다면
        if Y < M-1:
            # 동쪽으로 한칸 이동
            Y += 1
            # 동쪽으로 회전 시켰을 때에 맞추어 주사위의 값들 변경하기
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
            # 변경 후 보드의 현재 위치 값이 0 이라면
            if arr[X][Y] == 0:
                # 보드의 값에 다이스의 아랫면
                arr[X][Y] = dice[1]
            # 0이 아니라면
            else:
                # 반대로 진행
                dice[1] = arr[X][Y]
                arr[X][Y] = 0
            # 가장 윗면의 값 넣기
            ans.append(dice[0])

    if i == 2:
        if Y > 0:
            Y -= 1
            dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]

            if arr[X][Y] == 0:
                arr[X][Y] = dice[1]

            else:
                dice[1] = arr[X][Y]
                arr[X][Y] = 0

            ans.append(dice[0])

    if i == 3:
        if X > 0:
            X -= 1
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]

            if arr[X][Y] == 0:
                arr[X][Y] = dice[1]

            else:
                dice[1] = arr[X][Y]
                arr[X][Y] = 0

            ans.append(dice[0])

    if i == 4:
        if X < N-1:
            X += 1
            dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]

            if arr[X][Y] == 0:
                arr[X][Y] = dice[1]

            else:
                dice[1] = arr[X][Y]
                arr[X][Y] = 0

            ans.append(dice[0])

print(*ans)