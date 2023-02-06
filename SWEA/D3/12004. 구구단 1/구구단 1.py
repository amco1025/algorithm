T = int(input()) # 테스트 케이스 수 입력
answer =[] # 구구단 숫자 저장할 리스트 생성

for i in range(1, 10): # 반복문을 통하여 구구단 하면서 수를 answer에 저장
    for j in range(1, 10):
        answer.append(i*j)
        
for tc in range(1, T+1):
    n = int(input()) # 수를 입력하고 그 값이 answer에 있으면 yes 아니면 no
    if n in answer:
        print("#"+str(tc)+" "+"Yes")
    else:
        print("#"+str(tc)+" "+"No")