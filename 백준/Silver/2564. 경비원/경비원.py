#x,y = map(int,input().split()) # 총 면적의 x값과 y값 입력
#n = int(input()) # 호출 횟수 입력
#distance = [] # 각 호출 위치의 거리 입력할 리스트 생성
#answer = [] # 최소거리를 나타낼 리스트 생성

#for _ in range(n + 1): # 호출 위치와 시작점을 나타낼 횟수 만큼 반복문 실행
#    direction, value = map(int, input().split()) # 남쪽의 x가 0인 점을 기준으로 일짜로 펴 각 점의 위치를 좌표로 표시 그 값을 distance에 저장
#    if direction == 1:
#        distance.append(2*x + y - value)
#    elif direction == 2:
#        if value == 0:
#            distance.append(0)
#        else:
#            distance.append(value)
#    elif direction == 3:
#        if value == 5:
#            distance.append(0)
#        else:
#            distance.append(2*x + y + value)
#    else:
#        distance.append(x + y - value)

#start = distance.pop() # 시작점이 가장 마지막에 입력되므로 pop을 사용하여 distance에서 뺴고 그 값을 start변수에 할당

#for i in distance: # 최소 거리를 계산하며 answer 리스트에 할당
#    if start > i:
#        if start - i > 2*x + 2*y - start + i:
#            answer.append(2*x + 2*y - start + i)
#        else:
#            answer.append(start - i)
            
#    elif i == start:
#        answer.append(0)
        
#    else:
#        if i - start > 2*x + 2*y - i + start:
#            answer.append(2*x + 2*y -i + start)
#        else:
#            answer.append(i - start)
#
#answer = sum(answer)
#print(answer) # answer를 더하여 출력

# 동쪽과 서쪽의 값이 주어지는 방법을 제대로 보지 않아 아래부터 위로 증가하는줄 알고 풀어 헤맸다.
# 좌표 계산을 잘못하여 오래 걸렸다.
x,y = map(int,input().split())
array = []
n = int(input())
for _ in range(n+1):
    position, value = map(int,input().split())
    if position == 1:
        array.append(y+value)
    elif position == 2:
        array.append(-value)
    elif position == 3:
        array.append(y-value)
    else:
        array.append(-x-y+value)

total = 2*x+2*y
cnt = 0
for i in range(n):
    val = array[n] - array[i]
    if val<0:
        val *= -1
    if total - val > val:
        cnt += val
    else:
        cnt += (total-val)
print(cnt)