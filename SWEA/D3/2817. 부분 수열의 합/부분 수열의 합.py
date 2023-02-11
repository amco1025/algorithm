T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    li = list(map(int, input().split()))
    n = len(li)
    answer = []
    for i in range(1, 1<<n):
        sm = 0
        for j in range(n):
            if i & (1<<j):
                sm += li[j]
        answer.append(sm)

    ans = 0

    for i in answer:
        if i == K:
            ans += 1
    print("#"+str(tc)+" "+str(ans))
