T = 10

for tc in range(1, T+1):
    n = int(input())
    a, b = map(int, input().split())
    li = []
    for i in range(b):
        li.append(a)

    ans = 1
    for i in li:
        ans = ans*i
    print("#"+str(tc)+" "+str(ans))