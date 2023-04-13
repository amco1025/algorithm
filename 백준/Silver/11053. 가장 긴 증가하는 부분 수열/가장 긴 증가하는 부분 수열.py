n = int(input())
li = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if li[i] > li[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))