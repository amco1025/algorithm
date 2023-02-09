T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    new_arr = [[0]*3 for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(3):
            answer=""
            if j == 0:
                for q in range(n):
                    answer = answer+str(arr[n-q-1][cnt])
            elif j == 1:
                for l in range(n):
                    answer = answer+str(arr[n-cnt-1][n-l-1])
            elif j == 2:
                for m in range(n):
                    answer = answer+str(arr[m][n-cnt-1])

            new_arr[i][j] = answer
        cnt = cnt + 1

    print("#"+str(tc))
    for i in new_arr:
        for j in i:
            print(j, end=' ')
        print()
