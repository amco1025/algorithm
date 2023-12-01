T = int(input())

for _ in range(T):
    n = int(input())
    li = list(map(int, input().split()))
    answer = [0 for _ in range(n)]
    flag = True

    answer[n-1] = li[n-1]+1
    test = [li[-1]+1]
    t = 0
    for i in range(n-2, -1, -1):
        test.sort()
        num = li[i] + 1
        t += 1
        for j in range(t):
            if num >= test[j]:
                num += 1


        if num > n:
            flag = False
            break
        else:
            answer[i] = num
            test.append(num)

    if flag:
        print(*answer)
    else:
        print('IMPOSSIBLE')



