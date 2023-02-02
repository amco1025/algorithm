T = int(input())  # 테스트케이스 수 입력

for tc in range(1, T+1): # 테스트 케이스 만큼 반복
    N = int(input()) # 버스 노선의 개수 입력
    answer = [] # 출력할 값을 저장할 리스트 생성
    final ="" # 조건에 맞추어 출력하기 위하여 변수 생성
    bus = [0] * 5001 #정류장의 수 길이 만큼 리스트 생성 후 아직 어떠한 노선도 입력하지 않았기 때문에 지나가는 노선의 수를 0으로 모두 초기화
    
    for i in range(N): # 노선의 수 만큼 반복
        A, B = map(int, input().split()) # 노선의 범위 설정
        for j in range(A, B+1): # 노선의 범위에 들어가는 정류장의 값을 1 증가
            bus[j] += 1
            
    p = int(input()) # 출력할 정류장 입력
    for _ in range(p):  # 문제 조건에 맞추어 출력할 값을 만들기
        c = int(input())
        answer.append(bus[c])
        
    final = final+str(answer[0])
    del answer[0]
    for k in answer:
        final = final+" "+str(k)
    
    print("#"+str(tc)+" "+str(final)) # 출력