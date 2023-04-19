import sys

N, S = map(int, input().split())
li = list(map(int, input().split()))

si = 0
ei = 0

ans = sys.maxsize
sm = 0

while True:
    if sm >= S:
        ans = min(ans, ei - si)
        sm -= li[si]
        si += 1

    elif ei == N:
        break

    elif ans == 1:
        break

    else:
        sm += li[ei]
        ei += 1


if ans == sys.maxsize:
    print(0)
else:
    print(ans)