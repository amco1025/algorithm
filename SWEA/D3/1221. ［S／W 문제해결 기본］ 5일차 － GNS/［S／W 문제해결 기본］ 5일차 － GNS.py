T = int(input())   # 테스트케이스 입력
word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"] # 정해진 단어 리스트에 저장
answer = {} # 

for i in range(len(word)):
    answer[word[i]] = i   # 딕셔너리에 수에 word를 키로하고 그의 수를 값으로 하여 딕셔너리 생성
for order in range(1, T + 1):  # 1부터 T까지 넣으며 반복문 진행
    order2, N = input().split() # order2와 N에 문제 조건에 맞추어 입력 #n과 입력할 word의 수
    N = int(N) # 입력할 수의 개수를 정수 형태로 변경
    array = list(input().split()) # 정렬한 word를 array에 저장

    new_array = [] # 문제 조건에 맞추어 정렬 후 넣어줄 리스트 생성
    for i in range(N): # word의 수 만큼 반복
        new_array.append(answer.get(array[i]))  # 0일 떄 zro 1일때 one ... new_array에  저장

    new_array.sort() 
    print(f'{order2} ')

    for i in range(len(new_array)):
        print(word[new_array[i]], end=" ")
    print()