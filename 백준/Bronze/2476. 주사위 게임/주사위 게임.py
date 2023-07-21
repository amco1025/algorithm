n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
mx_ans = 0

for i in arr:
    li = [0]*7
    ans = 0
    for j in i:
        li[j] += 1

    if max(li) == 3:
        for p in range(7):
            if li[p] == 3:
                ans += 10000 + p*1000
                mx_ans = max(ans, mx_ans)

    elif max(li) == 2:
        for q in range(6,-1,-1):
            if li[q] == 2:
                ans += 1000+q*100
                mx_ans = max(ans, mx_ans)

    else:
        for w in range(6,-1,-1):
            if li[w] == 1:
                ans += w*100
                mx_ans = max(ans, mx_ans)
                break


print(mx_ans)