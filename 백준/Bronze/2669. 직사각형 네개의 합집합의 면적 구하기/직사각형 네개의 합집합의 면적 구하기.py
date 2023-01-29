paper = [[0]*100 for _ in range(100)] # 문제에 주어진 총 길이에 맞추어 아무것도 안채워진 종이 입력
answer = 0 # 출력할 변수 생성 후 0 할당

for _ in range(4): # 4번 종이 넣는다고 헀으니 4번 반복
    a, b, c, d = map(int, input().split()) # 양쪽 귀퉁이 입력
    for i in range(a,c): # 왼쪽 끝에서 오른쪽 끝까지 종이 넓이 만큼 1 할당
        for j in range(b,d):
            paper[i][j] = 1
            
for i in paper: # 1인 부분 즉 넓이 출력
    for j in i:
        if j == 1:
            answer = answer + 1
        else:
            continue
            
print(answer)