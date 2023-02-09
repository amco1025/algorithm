T = int(input())

for tc in range(1, T+1):
    answer = []
    li = list(map(int, input().split()))
    for i in li:
        if i < 40:
            answer.append(40)
        else:
            answer.append(i)
    answer = int(sum(answer) / len(answer))
    
    print("#"+str(tc)+" "+str(answer))