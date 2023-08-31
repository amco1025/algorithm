li = list(input())

for i in range(len(li)):
    if li[i] == 'w':
        li[i] = 1
    elif li[i] == 'o':
        li[i] = 2
    elif li[i] == 'l':
        li[i] = 3
    else:
        li[i] = 4

ans = 1

answer = [0] * 4

for i in range(len(li)):
    if li[i] == 1:
        answer[0] += 1

        if answer[1] != answer[2] or answer[1] != answer[3] or answer[2] != answer[3]:
            ans = 0
            break

    elif li[i] == 2:
        answer[1] += 1
        if answer[1] > answer[0]:
            ans = 0
            break
        if answer[2] != answer[3]:
            ans = 0
            break
    elif li[i] == 3:
        answer[2] += 1
        if answer[0] != answer[1]:
            ans = 0
            break
        if answer[2] > answer[1] or answer[2] > answer[0]:
            break

    elif li[i] == 4:
        answer[3] += 1
        if answer[0] != answer[1]:
            ans = 0
            break
        if answer[0] != answer[2]:
            ans = 0
            break
        if answer[1] != answer[2]:
            ans = 0
            break
        if answer[3] > answer[0] or answer[3] > answer[1] or answer[3] > answer[2]:
            ans = 0
            break


if answer[0] == answer[1] == answer[2] == answer[3] and ans == 1:
    print(1)
else:
    print(0)