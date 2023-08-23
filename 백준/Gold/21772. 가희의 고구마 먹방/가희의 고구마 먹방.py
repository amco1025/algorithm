import sys

input = sys.stdin.readline


def backtracing(cnt, gahee, sweetPotato):
    global max

    if cnt == T:
        if max < sweetPotato:
            max = sweetPotato
        return

    # 위로 움직
    gahee[0] -= 1
    if gahee[0] >= 0:
        move([0, -1], cnt, gahee, sweetPotato)
    else:
        gahee[0] += 1

    # 아래로 움직
    gahee[0] += 1
    if gahee[0] < R:
        move([0, 1], cnt, gahee, sweetPotato)
    else:
        gahee[0] -= 1

    # 좌로 움직
    gahee[1] -= 1
    if gahee[1] >= 0:
        move([1, -1], cnt, gahee, sweetPotato)
    else:
        gahee[1] += 1

    # 우로 움직
    gahee[1] += 1
    if gahee[1] < C:
        move([1, 1], cnt, gahee, sweetPotato)
    else:
        gahee[1] -= 1


def move(direction, cnt, loc, sweet):
    if arr[loc[0]][loc[1]] == '#':
        loc[direction[0]] -= direction[1]
    else:
        if arr[loc[0]][loc[1]] == 'S':
            arr[loc[0]][loc[1]] = '.'
            backtracing(cnt + 1, loc, sweet + 1)
            arr[loc[0]][loc[1]] = 'S'
        else:
            backtracing(cnt + 1, loc, sweet)
        loc[direction[0]] -= direction[1]

R, C, T = list(map(int, input().split()))

arr = list(list(input()) for _ in range(R))
max = 0
sweetPotato = 0
for i in range(R):
    if 'G' in arr[i]:
        gahee = [i, arr[i].index('G')]
backtracing(0, gahee, sweetPotato)

print(max)