T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    answer = 0
    for i in range(1, n-1):
        if (min(li[i-1], li[i], li[i+1]) != li[i]) & (max(li[i-1], li[i], li[i+1]) != li[i]):
            answer += 1
        else:
            continue
    print("#"+str(tc)+" "+ str(answer))