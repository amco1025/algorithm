def DFS(j, row, col, num):  # DFS 함수 만들기
    dx = [1,-1,0,0] # 좌1칸 우1칸
    dy = [0,0,1,-1] # 아래 1칸 위 1칸
    num += arr[row][col] # 배열에 다음오는 ㄱ밧을 이은다.
    if j == 6: # 만약 길이가 6이라면 answer에 그 값을 추가
        answer.append(num)
        return
    for i in range(4): # i에 0부터 3까지 넣으며 반복
        if 0<=row+dx[i]<4 and 0<=col+dy[i]<4: # 만약 움직인 후 범위 안에 있다면
            DFS(j+1, row+dx[i], col+dy[i], num) # 다시 DFS


T = int(input()) # 테스트 케이스 입력

for tc in range(1, T+1): # 테이스 케이스 만큼 반복
    arr = [list(map(str, input().split())) for _ in range(4)] # 행렬 입력
    answer = [] # 6길이 된 글자 추가할 리스트
    for x in range(4):     # 16군데 모든점에서 시작하여 DFS진행
        for y in range(4):
            DFS(0,x,y,"")

    answer = set(answer) # 중복값 제거
    print("#"+str(tc)+" "+str(len(answer)))
