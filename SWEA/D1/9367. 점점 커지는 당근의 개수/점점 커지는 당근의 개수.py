T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    cnt = 1
    answer = []
    for i in range(n-1):
        if li[i] < li[i+1]:
            cnt += 1
            answer.append(cnt)
        else:
            answer.append(cnt)
            cnt = 1
    mx = 1
    for i in answer:
        if i > mx:
            mx = i
        else:
            continue
    print("#"+str(tc)+" "+str(mx))