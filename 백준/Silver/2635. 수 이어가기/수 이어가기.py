start = int(input()) # 시작 수 입력
nums = [] # 조건에 맞는 수들이 들어갈 리스트 생성

for i in range(1, start + 1): # 1 부터 시작 값 까지 넣으며 반복문 진행
    li = [start] # 진행중인 현재 리스트에 시작 값 할당
    li.append(i) # 진행중인 현재 리스트에 반복문의 i 할당
    cnt = 1 # 인덱스를 표시 위하여 cnt 볕수 만들기
    
    while True:
        next_num = li[cnt-1] - li[cnt] # 문제 조건을 만족할 떄 까지 반복문 진행
        if next_num < 0: 
            break
        else:
            li.append(next_num) # 만족시 현재 진행중인 리스트에 추가
            cnt = cnt + 1 # 인덱스 번호 1 증가
        
    if len(nums) < len(li): # 전 리스트 중 가장 길이가 긴 것 보다 지금 진행중인게 더 길다면 변경
        nums = li
    else:
        continue
        
print(len(nums)) # 문제 조건에 맞추어 출력

answer = str(nums[0])
for i in nums[1:]:
    answer = answer+" "+str(i)
print(answer)