T = 10

for tc in range(1, T+1):
    n = int(input())
    a = input()
    stk = []
    answer = []
    answer_1 = []

    for i in a:
        if i == '+':
            if len(stk) == 0:
                stk.append(i)
            else:
                while len(stk) > 0:
                    answer.append(stk.pop())
                stk.append(i)

        else:
            answer.append(i)

    for i in stk:
        answer.append(i)

    for i in answer:
        if i == '+':
            a = int(answer_1.pop())
            b = int(answer_1.pop())
            answer_1.append(a+b)
        else:
            answer_1.append(i)

    print("#"+str(tc)+" "+str(answer_1[0]))
