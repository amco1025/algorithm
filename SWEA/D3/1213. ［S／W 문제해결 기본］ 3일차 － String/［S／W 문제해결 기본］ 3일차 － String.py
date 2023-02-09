for _ in range(10):
    n = int(input())
    k = input()
    N = len(k)
    st = input()
    answer = 0
    for i in range(len(st)-N+1):
        a = ""
        for j in range(i,i+N):
            a = a+st[j]
        if a == k:
            answer += 1
    print("#"+str(n)+" "+str(answer))
