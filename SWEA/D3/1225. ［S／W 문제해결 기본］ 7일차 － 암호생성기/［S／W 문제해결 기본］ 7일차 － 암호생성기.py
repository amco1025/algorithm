T = 10

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))

    while 0 not in li:
        for i in range(1, 6): # 1~5 감소하는게 한 주기 이므로 i에 1~5넣으며 반복
            p = li.pop(0) # 가장 앞에 있는거에서 i를 빼고 제일 뒤로 보냄
            p = p - i
            if p <= 0: # 0보다 작거나 같아지면 0을 맨뒤에 넣고 반복문 종료
                p = 0
                li.append(p)
                break
            else:
                li.append(p)


    ans = ""
    ans =ans+str(li[0])
    del li[0]
    for i in li:
        ans=ans+" "+str(i)
    print("#"+str(tc)+" "+ans)