T = int(input()) # 테스트 케이스 수 만큼 반복

for tc in range(1, T+1):
    D, L, N = list(map(int, input().split())) # 데미지, 레벨, 횟수 입력
    answer = 0 # 입힌 데미지 변수 만들고 0할당
    for i in range(0, N): # 반복
        answer += D*(1 + i*L/100) # 문제에서 주어진 식에 따라 answer에더함
    answer = int(answer)
    print("#"+str(tc)+" "+str(answer))