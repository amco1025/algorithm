def inorder(t):
    if t:
        inorder(L[t])
        ans.append(a[t-1])
        inorder(R[t])


T = 10
for tc in range(1, T+1):
    N = int(input())
    a = []
    L = [0] * (N+1)
    R = [0] * (N+1)
    ans = []
    for _ in range(N):
        li = list(map(str, input().split()))
        if len(li) == 2:
            a.append(li[1])
        elif len(li) == 3:
            a.append(li[1])
            L[int(li[0])] = int(li[2])
        elif len(li) == 4:
            a.append(li[1])
            L[int(li[0])] = int(li[2])
            R[int(li[0])] = int(li[3])


    inorder(1)
    print(f'#{tc}', "".join(ans))