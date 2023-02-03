T = int(input())
 
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    answer = [0] * N
    for i in range(1, Q+1):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            answer[j] = i
             
    final = ""
    final = final+str(answer[0])
    del answer[0]
    for k in answer:
        final = final+" "+str(k)
    print("#"+str(tc)+" "+final)
