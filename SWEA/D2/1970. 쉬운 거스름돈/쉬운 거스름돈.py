T = int(input()) # 테스트 수 입력
won = [50000, 10000, 5000, 1000, 500, 100, 50, 10] #거스름 돈 종류 리스트
 
for tc in range(1, T+1): # 테스트 케이스 수 만큼 반복
    answer = [0] * 8 # 출력할 리스트 생성
    n = int(input()) # 주어야 할 거스름돈 입력
    k = 0 # 각각의 거스름돈 수 알려줄 변수 생성
    for i in won: # 거스름돈의 값이 큰 지폐부터 넣으며 반복문 진행
        if n / i >= 1: # 몫이 1보다 크다면 몫 만큼 리스트에 저장하고 그 만큼 거스름돈에서 뺌
            answer[k] = n//i
            k = k + 1
            n = n - i * (n//i)
        else:
            k = k + 1
    final = "" # 문제 조건에 맞추어 출력
    final = final + str(answer[0])
    del answer[0]
    for i in answer:
        final = final+" "+str(i)
        
    print("#"+str(tc))
    print(final)