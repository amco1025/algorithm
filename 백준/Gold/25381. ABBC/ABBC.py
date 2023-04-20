li = list(str(input()))

ans = 0

answer = []
final = []
for i in range(len(li)-1, -1, -1):
    if li[i] == 'A' and 'B' in answer:
        answer.remove('B')
        ans += 1


    else:
        answer.append(li[i])

for i in range(len(answer)):
    if answer[i] == 'B' and 'C' in final:
        final.remove('C')
        ans += 1


    else:
        final.append(answer[i])

print(ans)