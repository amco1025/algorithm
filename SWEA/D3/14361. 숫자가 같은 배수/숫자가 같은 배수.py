T = int(input())                   # 테스트 케이스 수 입력

for tc in range(1, T+1):        # 테스트 케이스 만큼 반복
    n = int(input())               # 확인할 수 입력
    li = []                           # 배수로 한 값을 리스트로 저장할 리스트 생성
    answer = []                    # 배수로 된 수를 각각 저장할 리스트 생성
    final = []                       #  입력한 수를 하나씩 나누어 리스트에 저장
    for i in range(2,10):
        li.append(i * n)
    for j in range(len(li)):       # 배수로 된 값을 하나씩 리스트에 저장 저장할 떄 정렬하여 저장
        cnt = []
        for k in str(li[j]):
            cnt.append(int(k))
        cnt.sort()
        answer.append(cnt)
        
    for p in str(n):
        final.append(int(p))

    final.sort()
    
    if final in answer:                          # 만약 원래값을 정렬한 것이 배수에 있으면 possibla 아니라면 impossible
        print("#"+str(tc)+" "+"possible")
    else:
        print("#"+str(tc)+" "+"impossible")
