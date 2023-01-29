N = int(input()) # 학생 수 입력
num = list(map(int, input().split())) # 뽑은 숫자 입력
line = [] # 뽑은 숫자에 따른 줄

for i in range(N): # 뽑아서 변경된 수를 line에 저장
    line.insert(i-num[i], i+1) # 원래 자리에서 뽑은 숫자에 따른 뺀 인덱스에 학생 저장
    
answer = str(line[0]) # 조건에 맞추어 출력값 형성

for i in line[1:]:
    answer = answer+" "+str(i)
    
print(answer) # 출력