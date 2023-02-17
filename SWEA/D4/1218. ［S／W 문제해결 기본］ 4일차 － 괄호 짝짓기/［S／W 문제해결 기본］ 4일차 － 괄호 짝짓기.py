T = 10

for tc in range(1, T+1):
    n = int(input())
    a = input()
    stack = [] # 여는 괄호를 저장할 리스트 생성
    answer = 1 # 시작을 성공으로 할당 후 반복문 실행
    for i in range(n):
        if a[i] == '{' or a[i] == '[' or a[i] == '(' or a[i] == '<': # 여는 괄호 일 때는 스택에 저장
            stack.append(a[i])

        elif a[i] == ']': # 닫는 괄호라면
            if '[' not in stack: # 짝이 맞는 여는 괄호가 stack에 없다면 asnwer = 0으로 바꾸고 반복문 끝냄
                answer = 0
                break
            else: # 아니라면 여는 괄호 하나를 스택에서 제거
                stack.remove('[')
        elif a[i] == ')':
            if '(' not in stack:
                answer = 0
                break
            else:
                stack.remove('(')

        elif a[i] == '}':
            if '{' not in stack:
                answer = 0
                break
            else:
                stack.remove('{')
        elif a[i] == '>':
            if '<' not in stack:
                answer = 0
                break
            else:
                stack.remove('<')
    if len(stack) != 0: # 스택에 여는 괄호가 남아 있다면 answer 에 0 넣기
        answer = 0


    print("#"+str(tc)+" "+str(answer))