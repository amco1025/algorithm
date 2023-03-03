T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]
    answer = ''

    for j in range(15):
        for i in range(5):
            if len(arr[i]) > j:
                answer += arr[i][j]
    print("#"+str(tc)+" "+answer)