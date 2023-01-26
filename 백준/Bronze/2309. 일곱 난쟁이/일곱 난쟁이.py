li = [0] * 9 # 9명의 정보가 입력되므로 길이가 9인 리스트 생성

for i in range(9): # 9번 반복하며 값 입력하며 리스트에 할당
    li[i] = int(input())
    
li.sort() # li 정렬

answer = sum(li) - 100  # 총 더한 값에서 100을 뺸 값을 answer에 저장


for i in range(9):      # 반복하여 값을 넣어주며 2개의 값의 합이 answer이 되는 i와 j를 만들어 놓은 변수에 저장
    for j in range(i+1, 9):
        if li[i] + li[j] == answer: # 만약 i번쨰 값과 j번쨰 값의 합이 answer와 같다면 
            for k in range(len(li)): # i번째 값과 j번째 값만 빼면서 춝력
                if k == i or  k == j:
                    pass
                else:
                    print(li[k])
            exit()