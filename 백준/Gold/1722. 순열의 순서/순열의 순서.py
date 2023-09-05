N = int(input())
tmp = list(map(int,input().split()))
c, numbers = tmp[0],tmp[1:]
factorial = [0]*21
factorial[0] = 1
for i in range(1,21):
    factorial[i] = factorial[i-1]*i

if c==1:
    answer = []
    numbers = numbers[0]
    used = [0]*(N+1)
    for i in range(N):
        for j in range(1,N+1):
            if used[j]==1:
                continue
            ans = factorial[N-i-1]
            if factorial[N-i-1]<numbers:
                numbers-=factorial[N-i-1]
            else:
                used[j]=1
                answer.append(j)
                break
    print(*answer)
elif c==2:
    answer = 0
    used = [0]*(N+1)
    for i in range(N):
        for j in range(1,numbers[i]):
            if used[j] == 0:
                answer += factorial[N-1-i]
        used[numbers[i]] = 1
    print(answer+1)