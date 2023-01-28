N = int(input())     # 색종이의 수 입력

paper = [[0 for _ in range(101)] for _ in range(101)] # 종이 크기에 맞는 리스트 생성
black = 0 # 검은 곳 수 처음 0 할당

for _ in range(N): # 종이 수 만큼 반복문 진행
    x, y = map(int, input().split()) # 좌표 입력
    for i in range(x, x+10): # 좌우의 길이와 상하의 길이가 10 이므로 그 만큼 1을 입력
        for j in range(y, y+10):
            paper[i][j] = 1

for i in paper: # 리스안에 리스트를 돌며 값이 1이면 출력할 값인 black 에 1을 더함
    for j in i:
        if j == 1:
            black = black + 1
        else:
            continue

print(black)