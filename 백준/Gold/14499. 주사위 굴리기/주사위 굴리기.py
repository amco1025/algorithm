N, M, X, Y, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
li = list(map(int, input().split()))

# 위, 아래, 앞, 뒤, 오, 왼
dice = [0,0,0,0,0,0]
ans = []
for i in li:
    if i == 1:
        if Y < M-1:
            Y += 1
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]

            if arr[X][Y] == 0:
                arr[X][Y] = dice[1]

            else:
                dice[1] = arr[X][Y]
                arr[X][Y] = 0

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