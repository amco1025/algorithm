T = 10                                            # 문제에서 주어진 테스트케이스 수 입력
                              
for tc in range(1, T+1):                      # 테스트케이스 수 만큼 반복
  n = int(input())                               # 옮기는 횟수 입력
  height = list(map(int, input().split()))    # 덤프의 높이를 리스트에 저장
  answer = 0                                   # 최댓값 - 최솟값을 나타낼 변수 생성 후 0 할당
  for _ in range(n):                           # 주어진 횟수 만큼 반복
    height.sort()                               # 정렬
    
    if height[-1] - height[0] <= 1:       # 만약 최대 - 최소 가 1이하라면
      answer = height[-1] - height[0]  # 출력
      print("#"+str(tc)+" "+str(answer))
      break
    
    elif height[-1] - height[0] > 1: # 아니라면 최소 +1 최대 -1
        height[0] += 1
        height[-1] -= 1
        height.sort()
        continue
            
  answer = height[-1] - height[0]
  print("#"+str(tc)+" "+str(answer)) # 출력