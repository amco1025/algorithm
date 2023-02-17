T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [0] * 401 # 1번방과 2번방의 사이를 visited[1] 3번방과 4번방 사이를 visited[2]로 나타낼 수 있도록 visited 리스트 생성
    for _ in range(N): # 움직이는 학생수 만큼 반복
        A, B = map(int, input().split())
        if A < B:
            if A % 2 == 1: # A,B 가 홀수 짝수 일때를 나누어 각각의 경우 복도의 몇번칸 부터 몇번칸 까지 사용하는지 확인후 1씩 더하기
                if B % 2 == 1:
                    for i in range(A//2 + 1, B//2 + 2):
                        visited[i] += 1
                else:
                    for i in range(A//2 + 1, B//2 + 1):
                        visited[i] += 1
            else:
                if B % 2 == 1:
                    for i in range(A//2, B//2 + 2):
                        visited[i] += 1
                else:
                    for i in range(A//2, B//2 + 1):
                        visited[i] += 1
        else:
            if A % 2 == 1: # A,B 가 홀수 짝수 일때를 나누어 각각의 경우 복도의 몇번칸 부터 몇번칸 까지 사용하는지 확인후 1씩 더하기
                if B % 2 == 1:
                    for i in range(B//2 + 1, A//2 + 2):
                        visited[i] += 1
                else:
                    for i in range(B//2 , A//2 + 2):
                        visited[i] += 1
            else:
                if B % 2 == 1:
                    for i in range(B//2+1, A//2 + 1):
                        visited[i] += 1
                else:
                    for i in range(B//2, A//2 + 1):
                        visited[i] += 1
    print("#"+str(tc)+" "+str(max(visited))) # 복도에 표시된 것중 최댓값 출력