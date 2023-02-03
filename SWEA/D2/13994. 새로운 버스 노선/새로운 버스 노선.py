T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = 0
 
    cnts = [0]*1001
    for _ in range(N):  # N번 반복 처리
        B, S, E = map(int, input().split())
        if B==1:        # 일반버스
            for i in range(S, E+1):
                cnts[i] += 1
        elif B==2:      # 광역버스
            cnts[E]+=1  # 홀수이던 짝수이던 무조건 도착역에는 정차
            for i in range(S, E, 2):
                cnts[i]+=1
        else:           # 광역급행
            cnts[S]+=1
            cnts[E]+=1
            for i in range(S+1,E):
                # 시작이 짝수이면서 4의배수  또는 시작이 홀수 & 3의배수 & 10의배수아님
                if (S%2==0 and i%4==0) or (S%2!=0 and i%3==0 and i%10!=0):
                    cnts[i]+=1
 
    for n in cnts:  # 최대값 찾기
        if ans<n:
            ans=n
 
    print(f'#{test_case} {ans}')
    
    # 다시 풀어보기
