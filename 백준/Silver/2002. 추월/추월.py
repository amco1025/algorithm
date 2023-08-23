n = int(input())
li = []

for i in range(n):
    a = input()
    li.append(a)

ans = []
for i in range(n):
    a = input()
    ans.append(a)

sol = [0 for _ in range(n)]

time = 0
for i in li:
    time += 1
    for j in range(n):
        if ans[j] == i:
            sol[j] = time

answer = 0

for i in range(n):
    for j in range(i+1, n):
        if sol[i] > sol[j]:
            answer += 1
            break

print(answer)