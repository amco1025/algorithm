T = int(input()) # 테스트 케이스 수 입력

for tc in range(1, T+1): # 반복
    n = int(input()) # 정사각형 길이 입력
    arr = [list(map(int, input())) for _ in range(n)] # 리스트의 각 부분에 농작물 수 입력
    answer = 0 # 출력할 총합 변수 만들고 0 할당
    mid = n // 2 # 중앙
    r = 1 # 더해야할 밭 수
    for i in range(n//2 + 1):          # 중앙까지 반복하며 더함
        answer = answer + sum(arr[i][mid:mid+r])
        r += 2
        mid -= 1

    mid_1 = 1
    r_1 = n-2
    for j in range((n//2)+1, n):      # 중앙 뒤 부터는 밭 수를 감소 시키면서 더함
        answer = answer + sum(arr[j][mid_1:mid_1+r_1])
        mid_1 += 1
        r_1 -= 2

    print("#"+str(tc)+" "+str(answer))
