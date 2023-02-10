T = int(input())

for _ in range(T):
    a = input()
    a = list(a)
    n = len(a)
    arr = [['.']*(4*n + 1) for _ in range(5)]
    cnt = 0
    for i in range(2,4*n+1, 4):
        arr[2][i] = a[cnt]
        cnt += 1

    for i in range(5):
        if i == 0 or i ==4:
            for j in range(2, 4*n+1, 4):
                arr[i][j] = "#"
        elif i == 1 or i == 3:
            for q in range(1, 4*n+1, 2):
                arr[i][q] = "#"
        elif i == 2:
            for w in range(0, 4*n+1, 4):
                arr[i][w] = "#"
    for i in arr:
        print("".join(map(str, i)))