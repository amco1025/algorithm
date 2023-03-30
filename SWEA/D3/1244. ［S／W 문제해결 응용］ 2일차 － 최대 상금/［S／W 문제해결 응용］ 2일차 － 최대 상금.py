T = int(input())

def dfs(cnt, li):
    global ans
    
    # 가지 치기
    if (cnt, int(''.join(li))) in check:
        return

    check.add((cnt, int(''.join(li))))

    # 종료 조건
    if cnt == 0:
        ans = max(ans, int(''.join(map(str, li))))
        return
    # 하부 조건
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            li[i], li[j] = li[j], li[i]
            dfs(cnt-1, li)
            li[i], li[j] = li[j], li[i]


for tc in range(1, T+1):
    li, N = input().rstrip().split()
    li = list(li)
    N = int(N)
    check = set()
    ans = -1

    dfs(N, li)
    print("#"+str(tc)+" "+str(ans))