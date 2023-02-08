# T = int(input())        # 테스트 케이스 수 입력
# 
# for tc in range(1, T+1): # 테스트 케이스 만큼 반복
#     N = int(input()) # 문제의 수 입력
#     li = list(map(int, input().split())) # 문제의 각 점수를 리스트에 저장
#     answer = set() # 부분집합의 합을 넣을 리스트 생성
#     n = len(li)
#     final = []
#     for i in range(1, 1<<n): # 부분집합의 합을 answer리스트에 저장
#         sm = 0
#         for j in range(n):
#             if i & (1<<j):
#                 sm += li[j]
#         answer.add(sm)
#     answer.add(0) # 0 추가
#     answer = len(answer) # 중복값을 지운 후 길이
#     final.append(answer)
# 
#     for i in final:
#         print("#"+str(tc)+" "+str(i))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 시험 문항 수
    score = list(map(int, input().split()))  # 문항 별 점수
    answer = [0]  # 0점부터 시작

    for s in score:
        answer = list(set(answer))  # 중복 점수 제거
        for i in range(len(answer)):
            answer.append(answer[i] + s)

    print('#' + str(test_case), len(set(answer)))