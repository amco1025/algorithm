T = int(input()) # 테스트 케이스 수 입력

for tc in range(1, T+1): # 수 만큼 반복문 진행
    N, K = map(int, input().split()) # 과목수와 더할 수 입력
    a = list(map(int, input().split())) # 받은 점수 리스트에 저장
    a.sort(reverse = True) # 내림차순으로 정렬
    answer = 0 # 출력할 변수 생성 후 0 할당
    for i in range(K): # 더할 과목수 만큼 반복문 진행하며 큰 값 부터 더함
        answer = answer + a[i]
    print("#"+str(tc)+" "+str(answer)) # 조건에 맞추어 출력
