T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    A = list(A)
    N = len(A)
    n = len(B)
    answer = 0

    for i in range(N-n+1):
        a = ""
        for j in range(i, i+n):
            a = a+A[j]
        if a == B:
            answer += 1
            for k in range(n):
                A[i+k] = '@'
    mi = (n-1) * answer
    answer = N - mi

    print("#"+str(tc)+" "+str(answer))
