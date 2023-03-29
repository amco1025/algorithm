from itertools import combinations


def cook(li):
    sm = 0
    for i, j in combinations(li,2):
        sm += arr[i][j] + arr[j][i]
    return sm

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    li = [n for n in range(N)]
    ans = 100000
    ans_1 = []
    ans_1 = ans_1+list(combinations(li,N//2))
    for i in ans_1:
        ans_2 = [n for n in range(N)]
        for j in i:
            ans_2.remove(j)
        i = list(i)

        sm_1 = cook(i)
        sm_2 = cook(ans_2)

        ans = min(ans, abs(sm_1-sm_2))
        if ans == 0:
             break
    print("#"+str(tc)+" "+str(ans))