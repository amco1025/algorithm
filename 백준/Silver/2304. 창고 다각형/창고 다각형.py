n = int(input()) # 기둥의 개수 입력

lst = [] # 기둥의 위치와 높이를 입력할 리스트 생성
result = 0 # 출력할 결과 값에 초기값 0 할당

for i in range(n) : # 기둥의 개수만큼 반복하며 위치와 높이를 입력받고 리스트에 할당.
    a,b = map(int,input().split())
    lst.append([a,b])

lst.sort() # 리스트를 기둥의 위치 순서대로 정렬

i = 0   # 가장 높은 기둥을 기준으로 계산 해야 하므로 가장 높은 기둥 찾기
for l in lst :
    if l[1] > result :
        result = l[1]
        idx = i
    i += 1


height = lst[0][1] # 초기 기둥의 높이를 height 변수에 할당.


for i in range(idx) :  # 처음부터 가장높은 기둥까지 밑의 넓이 계산
    if height < lst[i+1][1] : # 현재 기둥보다 다음 기둥이 높은지 낮은지를 나누어 계산
        result += height * (lst[i+1][0]-lst[i][0])
        height = lst[i+1][1]
  
    else :
        result += height * (lst[i+1][0] - lst[i][0])


height = lst[-1][1]   # 앞에 한 과정 뒤에서부터 반복

for i in range(n-1, idx, -1) :
    if height < lst[i-1][1] :
        result += height * (lst[i][0]-lst[i-1][0])
        height = lst[i-1][1]
    else :
        result += height * (lst[i][0] - lst[i-1][0])

print(result) # 결과 값 출력

# 어려웠던 점
# 처음 리스트 안에 튜플을 넣어 위치와 높이를 같이 저장할 생각을 하지 못하여 창고의 길이 만큼
# 리스트를 기둥의 위치에 맞는 리스트에 기둥 높이를 넣을려고 하여 어려웠다.