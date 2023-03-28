def price(i, cost):
    global ans
    # 가지치기
    if cost > ans:
        return

    # 종료 조건
    if i >= 12:
        ans = min(cost, ans)
        return

    # 하부 조건
    # 만약 현재 인덱스 값이 0 이 아니라면
    if li[i]:
        price(i+1, cost+(li[i] * d))
        price(i+1, cost+m)
        price(i+3, cost+m3)
        price(i+12, cost+y)
    else:
        price(i+1, cost)


T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    li = list(map(int, input().split()))

    ans = 1000000
    price(0,0)
    print("#"+str(tc)+" "+str(ans))