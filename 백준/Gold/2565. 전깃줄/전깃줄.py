n = int(input())
wire = []
dp = [0] * n
for i in range(n):
    wire.append(list(map(int, input().split())))

wire.sort(key = lambda x:x[0])
line = []
for i in wire:
    line.append(i[1])

for i in range(n):
    for j in range(i):
        if line[i] > line[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n-max(dp))