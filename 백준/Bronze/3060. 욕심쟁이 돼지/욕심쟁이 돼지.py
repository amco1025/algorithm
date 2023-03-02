T = int(input())

for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    cnt = 1
    while sum(li) <= N:
        for i in range(6):
            if i == 0:
                a = li[1] + li[5] + li[3] + li[0]
            if i == 1:
                b = li[0] + li[2] + li[4] + li[1]
            if i == 2:
                c = li[1] + li[3] + li[5] + li[2]
            if i == 3:
                d = li[2] + li[4] + li[0] + li[3]
            if i == 4:
                e = li[3] + li[5] + li[1] + li[4]
            if i == 5:
                f = li[0] + li[4] + li[2] + li[5]
        li[0], li[1], li[2], li[3], li[4], li[5] = a, b, c, d, e, f
        cnt += 1
    print(cnt)