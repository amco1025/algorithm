T = 10
for test_case in range(1, T + 1):
    _ = input()
    N = 100
    # 좌, 우 양쪽을 0으로 padding해서 입력
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(N) ]
  
    # [1] 시작위치(2) 찾기
    ci = N-1
    for j in range(1, N+1): # padding 을 했으므로 1 ~ N 까지 검색
        if arr[ci][j]==2:
            cj = j
            break
  
    # [2] N-1행 시작위치에서 위쪽으로 사다리이동
    while ci>0:
        arr[ci][cj]=0           # 재방문 방지
        if arr[ci][cj-1]:       # 왼쪽!
            cj-=1               # 이동
        elif arr[ci][cj+1]:     # 오른쪽!
            cj+=1               # 이동
        else:
            ci-=1               # 위쪽이동
  
    print(f'#{test_case} {cj-1}')
