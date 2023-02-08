T = int(input()) # 테스트 케이스 수 입력

for tc in range(1, T+1): # 반복
    N, B = map(int, input().split())     # 사람 수와 높이 입력
    li = list(map(int, input().split())) # 사람의 키 리스트 형식으로 저장
    n = len(li)
    answer = []
    final = []
    answer_1 = 0
    for i in range(1, 1<<n): # 부분집합의 합을 구하며 나올 수 있는 경우의 합 모두 저장
        sm = 0
        for j in range(n):
            if i & (1 << j):
                sm += li[j]
        answer.append(sm)

    for i in answer:  # 차외 값 저장
        if i >= B:
            final.append(i-B)

    answer_1 = min(final) # 차의 최소값 저장
    
    print("#"+str(tc)+" "+str(answer_1))
