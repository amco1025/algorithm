import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    dp = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[0][i] = 1

    for i in range(1, n+1):
        for j in range(i, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[n][n])