def dfs(i, sm):
    global ans_mn
    global ans_mx

    # 종료 조건
    # 수를 다 사용
    if i == N:
        ans_mn = min(sm, ans_mn)
        ans_mx = max(sm, ans_mx)
        return

    # 하부 조건
    # 넣을 수 있는 연산자를 모두 넣어보며 진행
    val = su[i]
    if visited[0] > 0:
        visited[0] = visited[0] - 1
        dfs(i+1, sm+val)
        visited[0] += 1

    if visited[1] > 0:
        visited[1] = visited[1] - 1
        dfs(i+1, sm-val)
        visited[1] += 1

    if visited[2] > 0:
        visited[2] = visited[2] - 1
        dfs(i+1, sm*val)
        visited[2] += 1

    if visited[3] > 0:
        visited[3] = visited[3] - 1
        dfs(i+1, int(sm/val))
        visited[3] += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = list(map(int, input().split()))
    su = list(map(int, input().split()))
    ans_mn = 10000000
    ans_mx = -1000000
    dfs(1, su[0])
    sol = ans_mx - ans_mn
    print("#"+str(tc)+" "+str(sol))