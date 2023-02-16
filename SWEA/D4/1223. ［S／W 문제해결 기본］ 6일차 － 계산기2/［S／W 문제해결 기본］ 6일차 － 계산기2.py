dic = {'+':1, '*':2} # 우선순위 저장
T = 10
for tc in range(1, T+1):
    n = int(input())
    st = input()
    eq =""
    stk = []

    for ch in st: # 숫자라면 출력할 문자열에 저장
        if ch.isdigit():
            eq += ch
        else:          # 연산자라면 우선순위를 비교하여 넣을려한느 연산자의 우선순위가 크거나 스택이 비어있으며 push
            if not stk:
                stk.append(ch)
            else: # 아니라면 조건(top연산자 보다 지금 연산자의 우선순위가 더 큼) 만족할 때 까지 pop한후 문자열에 저장
                while stk and dic[ch] <= dic[stk[-1]]:
                    eq += stk.pop()
                stk.append(ch)

    while stk: # 연산자가 남아있다면 문자열에 추가
        eq += stk.pop()

    answer = []

    for i in eq:
        if i == '*': # '*' 라면 앞에 answer에서 두 개 빼서 곱하고 answer에 추가
            a = int(answer.pop())
            b = int(answer.pop())
            answer.append(a*b)
        elif i == '+': # '+'라면 앞에 answer에서 두 개 빼서 더하고 answer에 추가
            a = int(answer.pop())
            b = int(answer.pop())
            answer.append(a+b)
        else:
            answer.append(int(i))

    print("#"+str(tc)+" "+str(answer[0]))