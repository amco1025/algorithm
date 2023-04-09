N, K = input().rstrip().split()
li = list(N)
M = len(str(N))
K = int(K)
check = set()
ans = -1


def dfs(cnt, li):
    global ans

    if (cnt, int(''.join(li))) in check:
        return

    check.add((cnt, int(''.join(li))))

    if cnt == 0:
        ans = max(ans, int(''.join(map(str, li))))
        return

    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if i == 0 and li[j] == '0':
                continue
            li[i], li[j] = li[j], li[i]
            dfs(cnt-1, li)
            li[i], li[j] = li[j], li[i]

    return ans


ans = dfs(K, li)
print(ans)