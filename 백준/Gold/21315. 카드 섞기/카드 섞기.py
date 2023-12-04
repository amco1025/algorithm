import math

def mix(range_, cnt):
    newCard = [0] * n
    idx = 0
    for i in range(range_ - cnt, range_):
        newCard[idx] = card[i]
        card[i] = 0
        idx += 1
    for i in range(n):
        if card[i] != 0:
            newCard[idx] = card[i]
            idx += 1
        card[i] = newCard[i]

def solve(k):
    range_ = n
    for i in range(1, k + 2):
        cnt = int(math.pow(2, k - i + 1))
        mix(range_, cnt)
        range_ = cnt

n = int(input())
result = [int(x) for x in input().split()]
card = [0] * n

for k1 in range(1, n):
    if math.pow(2, k1) > n:
        break
    for k2 in range(1, n):
        if math.pow(2, k2) > n:
            break
        card = [i + 1 for i in range(n)]
        solve(k1)
        solve(k2)
        isFinish = True
        for i in range(n):
            if result[i] != card[i]:
                isFinish = False
                break
        if isFinish:
            print(k1, k2)
            exit(0)
