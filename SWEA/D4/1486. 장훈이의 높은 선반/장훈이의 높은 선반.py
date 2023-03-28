def dfs(n,h):
    global ans
    # 가지 치기
    if h-H > ans:
        return
	# 종료 조건
    if n == N:
        if h-H >= 0:
            if h-H < ans:
                ans = h - H
        return
	# 하부 조건
    dfs(n+1, h)
    dfs(n+1, h + li[n])


T = int(input())
for tc in range(1, T+1):
    N, H = map(int, input().split())
    li = list(map(int, input().split()))

    ans = 10000

    dfs(0,0)

    print("#"+str(tc)+" "+str(ans))