T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(n)]
    cnt = 0

    for i in range(m): # 첫 줄은 무조건 하얀색 하얀색이 아니라면 하얀색으로 바꾸고 +1
        if arr[0][i] != 'W':
            cnt += 1
            arr[0][i] = 'W'

    for i in range(m): # 마지막 줄은 무조건 빨간색 빨간색이 아니라면 빨간색으로 바꾸고 +1
        if arr[n-1][i] != 'R':
            cnt += 1
            arr[n-1][i] = 'R'

    answer = 10000
    w = 0
    for i in range(0, n-2): # 첫 줄 부터 파랑 빨강을 최소로 넣을 수 있는 칸을 빼고 나머지를 하얀색으로 넣을 수 있는 모든 경우
        for j in range(m): # 흰색이 아니라면 +1
            if arr[i][j] != 'W':
                w += 1

        b = 0
        for k in range(i+1, n-1): # 흰색을 넣은 다음줄 부터 빨간색을 최소로 넣을 수 있는 칸을 빼고 나머지를 파랑으로 넣을 수 있는 모든 경우
            for p in range(m):
                if arr[k][p] != 'B':
                    b += 1

            r = 0
            for q in range(k+1, n): # 나머지 모두 빨간색으로 바꾸기
                for t in range(m):
                    if arr[q][t] != 'R':
                        r += 1

            ans = w+b+r
            if answer > ans:
                answer = ans
    sol = cnt + answer
    print("#"+str(tc)+" "+str(sol))