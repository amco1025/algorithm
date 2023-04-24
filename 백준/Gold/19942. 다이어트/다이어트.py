def dfs(a,b,c,d,n,cost,visited):
    global ans
    global answer
    global k

    if cost >= ans:
        return

    if a >= A and b >= B and c >= C and d >= D:
        if ans > cost:
            ans = cost
            answer = visited[:]
            k = 1
        elif ans == cost:
            answer.append(visited[:])
            k += 1
        return
    
    if n == N:
        if a >= A and b >= B and c >= C and d >= D:
            if ans > cost:
                ans = cost
                answer = visited[:]
                k = 1
            elif ans == cost:
                answer.append(visited[:])
                k += 1
        return



    visited.append(n+1)
    dfs(a+arr[n][0], b+arr[n][1], c+arr[n][2], d+arr[n][3], n+1, cost+arr[n][4], visited)
    visited.pop()
    dfs(a,b,c,d,n+1,cost,visited)

N = int(input())
k = 0
A, B, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1000000000
answer = []
dfs(0,0,0,0,0,0,[])

if k > 1:
    answer.sort()
    answer = answer[0]

answer.sort()
if ans == 1000000000:
    print(-1)
else:
    print(ans)
    print(*answer)
