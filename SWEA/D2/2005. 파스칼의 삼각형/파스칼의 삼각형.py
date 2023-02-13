T = int(input())

for tc in range(1, T+1):
    li = [1]
    stk = [1]
    n = int(input())
    print("#"+str(tc))
    print(*li)
    for i in range(1,n):
        N = i+1
        li = [0] * N
        li[0] = 1
        li[N-1] = 1
        for j in range(1, N-1):
            li[j] = stk[j-1] + stk[j]
        stk = li
        print(*li)

