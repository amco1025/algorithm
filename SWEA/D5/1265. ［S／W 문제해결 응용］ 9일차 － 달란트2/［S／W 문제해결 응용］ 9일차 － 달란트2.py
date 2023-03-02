T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = N//M
    li = [a] * M

    if N % M:
        b = N % M
        for i in range(b):
            li[i] = li[i] + 1

    ans = 1

    for i in li:
        ans = ans * i

    print("#"+str(tc)+" "+str(ans))