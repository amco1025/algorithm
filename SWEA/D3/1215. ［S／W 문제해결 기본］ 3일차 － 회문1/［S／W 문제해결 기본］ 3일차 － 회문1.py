T = 10 # 문제에서 주어진 테스트케이스 수 입력

for tc in range(1, T+1): # 테스트케이스 수 만큼 반복

    n = int(input()) # 문제에서 주어진 조건 길이 입력
    bingo = [list(input()) for _ in range(8)] # 문제에서 주어진 판의 길이 만큼 행렬 만들기
    cnt = 0 # 조건에 만족하는 수의 값을 출력해줄 변수 생성

    for i in range(0, 8): #  가로에서 만족하는 것
        for j in range(0, 8-n+1): 
            if bingo[i][j:j+n] == bingo[i][j:j+n][::-1]:
                cnt += 1
                
    for j in range(0, 8): # 세로에서 만족하는 것
        for i in range(0, 8-n+1):
            char = ''
            for ci in range(i, i+n):
                char += bingo[ci][j]
            if char == char[::-1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt)) # 출력