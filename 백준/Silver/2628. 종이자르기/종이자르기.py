x, y = map(int, input().split()) # 종이 크기 입력
n = int(input()) # 자르는 횟수 입력

x_length = [0, x] # 종이의 가로 길이 저장
y_length = [0, y] # 종이의 세로 길이 저장

for _ in range(n): # 자르는 횟수 만큼 반복
    a, b = map(int, input().split()) # 자르는 방향과 길이 입력
    if a == 0: # 세로 자르기
        y_length.append(b) # 세로 길이의 자르는 좌표 입력
    elif a == 1: # 마찬가지로 가로 반복
        x_length.append(b)
        
x_length.sort() # 잘린 위치 순으로 정렬
y_length.sort()

big = 0 # 출력할 가장 큰 크기 종이 변수 생성

for i in range(len(x_length) - 1): # 잘린 곳 만큼 반복
    for j in range(len(y_length) - 1): # 잘린 곳 만큼 반복
        width = x_length[i + 1] - x_length[i] # 가로 길이는 전에 잘린 곳 부터 지금 잘린 곳 까지
        height = y_length[j+1] - y_length[j] # 가로와 마찬가지
        big = max(big, width*height) # 곱한 값 중 가장 큰 값 출력
        
print(big)