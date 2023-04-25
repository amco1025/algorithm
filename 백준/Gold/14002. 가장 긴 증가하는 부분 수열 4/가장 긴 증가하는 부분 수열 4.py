N = int(input())
li = list(map(int, input().split()))
dp = [0]*N

for i in range(N):
    for j in range(i):
        if li[i] > li[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
x = max(dp)
ans = []

for i in range(N-1, -1, -1):
    if dp[i] == x:
        ans.append(i)
        x -= 1

answer = []
for i in ans:
    answer.append(li[i])

answer.sort()
print(*answer)