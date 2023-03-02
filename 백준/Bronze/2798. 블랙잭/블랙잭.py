N, M = map(int, input().split())
li = list(map(int, input().split()))

ans = 0
sm = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sm = li[i] + li[j] + li[k]
            if sm <= M and sm > ans:
                ans = sm

print(ans)