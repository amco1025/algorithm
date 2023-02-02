#T = int(input())

#for tc in range(1, T+1):
#    n = int(input())
#    a = list(map(int, input().split()))
#    answer = 0
#    for i in range(n-1):
#       mx = 0
#        plu = []
#       for j in range(i+1, n):
#            if a[i] < a[j]:
#                plu.append(a[j])
#                mx = max(plu)
#        if len(plu) > 0:
#            answer = answer + mx - a[i]
#        
#    print("#"+str(tc)+" "+str(answer))




T = int(input())

# T만큼 반복
for tc in range(1, T+1):
    # 자연수 N의 개수 입력
    N = int(input())
    # N 리스트 입력
    N_list = list(map(int, input().split()))

    # N_list의 마지막 값을 최대값으로 설정
    max_value = N_list[-1]
    # 이익 변수 초기화
    profit = 0

    # N-2번째 인덱스부터 0번째 인덱스까지 1씩 감소하면서 반복 순회
    for i in range(N-2, -1, -1):
        # 만약 현재 매매가가 최대값보다 크면 최대값을 변경
        if N_list[i] >= max_value:
            max_value = N_list[i]
        # 현재 매매가가 최대값보다 크지 않으면 차익을 profit 변수에 더해준다
        else:
            profit += max_value - N_list[i]
    
    # 결과 출력
    print('#{} {}'.format(tc, profit))
    
# 다음에 시간 줄이며 다시 풀기