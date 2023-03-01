T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = -100

    if a < b:
        for i in range(b-a+1):
            cnt = 0
            for j in range(a):
                cnt += A[j] * B[j+i]
            if cnt > ans:
                ans = cnt

    if b < a:
        for i in range(a-b+1):
            cnt = 0
            for j in range(b):
                cnt += A[j+i] * B[j]
            if cnt > ans:
                ans = cnt

    print("#"+str(tc)+" "+str(ans))