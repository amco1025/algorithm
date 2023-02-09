T = int(input()) # 테스트 케이스 수 입력

for tc in range(1, T+1):  # 테스트 케이스 수 만큼 반복
    A = input() # 변수들 입력 : 입력 2진수, 입력 3진수, 리스트로 변환한 2진수와 3진수, 변경 후 모든 경우의 수를 저장할 리스트 입력값의 길이, 10진수로 변환 후 저장할 리스트
    B = input()
    A = list(A)
    B = list(B)
    li_A = []
    li_B = []
    n = len(A)
    N = len(B)
    answer_a = []
    answer_b = []

    for i in range(n): # 변경 가능한 모든 경우의 수를 만들어 리스트에 저장
        a = A[0:]   # 처음 여기서 a = A를 사용하여 복사 깊이 문제가 있었다.
        if a[i] == '1':
            a[i] = '0'
            li_A.append(a)
        else:
            a[i] = '1'
            li_A.append(a)

    for i in range(N): # 변경 가능한 모든 경우의 수를 저장
        b = B[0:]
        if b[i] == '2':
            b[i] = '1'
            li_B.append(b)
            b = B[0:]
            b[i] = '0'
            li_B.append(b)
        elif b[i] == '1':
            b[i] = '2'
            li_B.append(b)
            b = B[0:]
            b[i] = '0'
            li_B.append(b)
        elif b[i] == '0':
            b[i] = '1'
            li_B.append(b)
            b = B[0:]
            b[i] = '2'
            li_B.append(b)

    for k in li_A: # 문자열로 저장된 2진수를 10진수로 변경
        answer = 0
        cnt = 1
        for i in range(len(A)):
            answer = answer + cnt*int(k[len(A)-i-1])
            cnt = cnt*2
        answer_a.append(answer)

    for k in li_B: # 문자열로 저장 된 3진수를 10진수로 변경
        answer = 0
        cnt = 1
        for i in range(len(B)):
            answer = answer + cnt*int(k[len(B)-i-1])
            cnt = cnt*3
        answer_b.append(answer)

    for i in answer_a: # 같은 값 찾아 출력
        if i in answer_b:
            print("#"+str(tc)+" "+str(i))

