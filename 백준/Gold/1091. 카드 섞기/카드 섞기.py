N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
card = []
answer = []
for i in range(N):
    answer.append(i%3)
for i in range(N):
    card.append(i)
ans = 0
first = []
for i in range(N):
    first.append(i)
for i in range(N):
    first[i] = S[first[i]]
cnt = 0
while answer != P:
    for i in range(N):
        card[i] = S[card[i]]
    for i in range(len(card)):
        answer[i] = card[i]%3
    if first == card:
        cnt += 1
    if cnt == 2:
        ans = -1
        break
    ans += 1

print(ans)
