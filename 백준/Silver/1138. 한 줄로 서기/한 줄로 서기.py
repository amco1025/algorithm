n = int(input())
li = list(map(int, input().split()))
ans = [0] * n

for i in range(n):
    m = li[i]

    if m == 0:
        for j in range(n):
            if ans[j] == 0:
                ans[j] = i+1
                break

    elif i == n-1:
        for j in range(n):
            if ans[j] == 0:
                ans[j] = n

    else:
        sm = 0
        N = 0
        for j in range(n):
            if ans[j] == 0:
                sm += 1

            if sm == m:
                for k in range(j+1, n):
                    if ans[k] == 0 and N == 0:
                        ans[k] = i+1
                        N = 1

print(*ans)