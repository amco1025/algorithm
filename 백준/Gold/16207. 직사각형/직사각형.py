n = int(input())
li = list(map(int, input().split()))

li.sort(reverse = True)

ans = []
visited = [0] * n
for i in range(len(li)-1):
    if li[i] == li[i+1]:
        if visited[i] == 0 and visited[i+1] == 0:
            ans.append(li[i])
            ans.append(li[i + 1])
            visited[i] = 1
            visited[i + 1] = 1
    elif li[i] == li[i+1] + 1:
        if visited[i] == 0 and visited[i + 1] == 0:
            ans.append(li[i]-1)
            ans.append(li[i+1])
            visited[i] = 1
            visited[i+1] = 1


a = len(ans)%4

for _ in range(a):
    ans.pop()

answer = 0
for i in range(0, len(ans)-3, 4):
    answer += ans[i] * ans[i+2]

print(answer)