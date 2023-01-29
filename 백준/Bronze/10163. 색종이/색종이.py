paper = [[0]*1001 for _ in range(1001)] # 문제에서 주어진 총 넓이 만큼 배열 생성

n = int(input()) # 색종이의 개수 입력

for i in range(1, n+1): # 종이 수 만큼 반복 진행
    a, b, c, d = map(int, input().split()) # 주어진 종이 입력 뒤에 입력 될 수록 앞에 있으므로 큰 수로 변경
    for j in range(a, a+c):
        for k in range(b, b+d):
            paper[j][k] = i
            
for i in range(1, n+1): # 종이 번호가 보인다는 것은 제일 앞에 있으므로 보이는 종이이다. 따라서 각 종이의 번호가 보이는 만큼 면적 그 값을 출력
    answer = 0
    for j in paper:
        for k in j:
            if k == i:
                answer = answer + 1
            else:
                continue
    print(answer)