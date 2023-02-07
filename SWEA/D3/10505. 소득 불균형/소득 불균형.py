T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    med = sum(li)/len(li)
    answer = 0
    for i in li:
        if i <= med:
            answer += 1
        else:
            continue
    print("#"+str(tc)+" "+str(answer))