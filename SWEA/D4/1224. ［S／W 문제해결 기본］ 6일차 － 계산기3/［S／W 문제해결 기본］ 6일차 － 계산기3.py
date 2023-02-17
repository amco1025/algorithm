T = 10
n_num = {'(': 0, ')': 0, '+' :1 ,'-':1, '*':2, '/':2} # 각 연산기호에 우선순위 부여

for tc in range(1, T+1):
    stack = []
    answer = []
    n = int(input())
    a = input()
    stack_1 = []
    for i in a: # 만약 피연산자라면
        if i not in n_num.keys():
            answer.append(i) # 리스트에 추가
        elif i == '(': # 여는 괄호라면
            stack.append(i) # 스택에 추가
        elif i == ')': # 닫는 괄호라면
            while stack[-1] != '(': # 스택의 top이 여는 괄호가 될 때 까지 answer에 피연산자 추가
                answer.append(stack.pop())
            stack.pop() # 여는 괄호 스택에서 뺌
        else: # 연산자라면 우선순위 규칙에 맞추어 현재 값이 들어 있는 연산자보다 우선순위가 높다면 push 아니라면 높아질 때 까지 pop
            if n_num[stack[-1]] < n_num[i]:
                stack.append(i)
            else:
                while n_num[stack[-1]] >= n_num[i]:
                    answer.append(stack.pop())
                stack.append(i)

    ans = ''
    for c in answer:
        ans += c
    sol = []

    for i in ans: # 후위 표기법으로 바꾼 것 계산 만약 연산자라면 리스트에 저장된 앞에 두 수를 꺼내어 계산 피연산자라면 리스트에 저장
        if i == "+":
            a = int(sol.pop())
            b = int(sol.pop())
            sol.append(int(a+b))
        elif i == "-":
            a = int(sol.pop())
            b = int(sol.pop())
            sol.append(int(b-a))
        elif i == "*":
            a = int(sol.pop())
            b = int(sol.pop())
            sol.append(int(a*b))
        elif i == "/":
            a = int(sol.pop())
            b = int(sol.pop())
            sol.append(int(b/a))
        else:
            sol.append(i)
    print("#"+str(tc)+" "+str(sol[0]))