def DFS(i,n,ans,v,N):
    global mn

    if ans > mn: # 만약 지금까지 더한것이 전에 끝까지 더한 것 보다 크다면 리턴
        return
    if n == N: # 끝까지 돌았는데 현재 값이 최솟값 보다 작다면 최솟값 변경
        if ans < mn:
            mn = ans
    else: # 아니라면
        for j in range(N): # j 에 처음부터 n-1까지 넣으며 아직 안 가본 열 이라면 1로 바꾸고 dfs
            if v[j] == 0:
                v[j] = 1
                DFS(i+1, n+1, ans+arr[i][j], v, N)
                v[j] = 0 # 다시 0으로 바꿈

    return mn

T = int(input())

for tc in range(1, T+1): 
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    ans = 0
    n = 0
    v = [0] * N

    for j in range(N): # 첫 줄의 모든 열에서 시작하며 반복문 실행
        mn = 10000 # 변경될 수 있도록 최솟값 설정
        DFS(0,n,ans,v,N) 

    print("#"+str(tc)+" "+str(mn))