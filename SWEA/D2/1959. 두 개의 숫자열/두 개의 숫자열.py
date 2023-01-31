T = int(input())  # 입력된 테스트케이스 횟수 입력

for tc in range(1, T+1): # 테스트케이스 만큼 반복
    n, m = map(int, input().split()) # n, m 길이 입력
    A = list(map(int, input().split())) # 첫 번쨰 리스트 만들기
    B = list(map(int, input().split())) # 두 번쨰 리스트 만들기
    answer = [] # 옮기면거 만들어진 값 입력할 리스트 만들기
    N = abs(m-n) + 1 # 길이를 뺀 절댓값에 1더한 만큼 반복문 진행
    for i in range(N):
        plus_1 = 0
        plus_2 = 0
        plus_3 = 0
        if n > m: # 만약 n이 m보다 크다면
            for k in range(m): # m만큼 반복문 진행 # 결과 값에 0 할당
                plus_1 = plus_1 + A[k+i] * B[k] # m의 길이 만큼 리스트의 번호를 1씩 증가하며 곱하여 더한 값을 answer리스트에 추가 반복문을 한번 돈 다음 던 긴 리스트에 인덱스를 1증가시켜 다시 반복문 진행
            answer.append(plus_1)
                
        elif n == m:
            for s in range(n):
                plus_3 = plus_3 + A[s] * B[s]
            answer.append(plus_3)
              
                
        else: # 위와 같은 과정 반복
            for j in range(n):
                plus_2 = plus_2 + A[j] * B[i+j]
            answer.append(plus_2)
            
    answer_1 = max(answer)  # 가장 큰 값 출력
    print("#"+str(tc)+" "+str(answer_1))
