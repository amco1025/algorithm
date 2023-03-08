T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    li = list((map(str, input())))
    test = [0] * N
    test.append(li)
    n = N // 4
    sol = []

    ans = [[0] * n for _ in range(4)]
    cnt = 0
    for i in range(4):
        for j in range(n):
            ans[i][j] = li[cnt]
            cnt += 1

    for p in range(4):
        num = ""
        for q in range(n):
            num += ans[p][q]
        sol.append(num)

    for _ in range(1,N):
        k = li.pop()
        li.insert(0,k)

        ans = [[0]*n for _ in range(4)]
        cnt = 0
        for i in range(4):
            for j in range(n):
                ans[i][j] = li[cnt]
                cnt += 1

        for p in range(4):
            num=""
            for q in range(n):
                num+=ans[p][q]
            sol.append(num)

    for i in range(len(sol)):
        sol[i] = "0x"+sol[i]

    for i in range(len(sol)):
        sol[i] = int(sol[i],16)

    sol = set(sol)
    sol = list(sol)
    sol.sort(reverse = True)

    final = sol[K-1]
    print("#"+str(tc)+" "+str(final))