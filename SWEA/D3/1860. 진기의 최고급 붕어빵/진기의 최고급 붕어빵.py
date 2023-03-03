T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    li = list(map(int, input().split()))
    mx = max(li)
    ans = 1
    # 붕어빵
    a = [0] * (mx+1)
    cnt = 0
    for i in range(M, mx+1, M):
        cnt += K
        a[i] = cnt
    for i in range(mx):
        if a[i+1] < a[i]:
            a[i+1] = a[i]
    # 사람
    b = [0] * (mx+1)
    for i in li:
        b[i] += 1
    for i in range(1,len(b)):
        if b[i] == 0:
            b[i] = b[i-1]
        else:
            b[i] = b[i] + b[i-1]

    answer = [0] * (mx+1)

    for i in range(mx+1):
        answer[i] = a[i] - b[i]

    for i in answer:
        if i < 0:
            ans = 0

    if ans == 0:
        print("#"+str(tc)+" "+"Impossible")
    else:
        print("#"+str(tc)+" "+"Possible")