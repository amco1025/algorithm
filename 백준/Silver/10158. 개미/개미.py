w, h = map(int, input().split()) # 총 넓이 입력
p, q = map(int, input().split()) # 현재 위치 입력
t = int(input()) # 이동 시간 입력

a = (p + t) // w # 가로 방향으로 반사 된 횟수 저장
b = (q + t) // h # 세로 방향으로 반사 된 횟수 저장

if a % 2 == 0: # 가로 방향으로 짝수 번 반사 됬다면 
    x = (p + t) % w # 가로의 총 합에서 가로 총 길이로 나눈 나머지 값이 현재 위치
else: # 홀수 번 반사 됬다면
    x = w - (p + t) % w # 가장 오른 쪽에서 총 합에서 나눈 나머지 값을 뺸 값이 현재 위치
    
if b % 2 == 0: # x 방향과 동일
    y = (q + t) % h
else:
    y = h - (q + t) % h
    
print(x, y)