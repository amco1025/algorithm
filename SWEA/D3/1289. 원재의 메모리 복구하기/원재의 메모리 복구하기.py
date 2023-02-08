T = int(input())

for tc in range(1, T+1):
    a = input()
    li = []
    for i in str(a):
        li.append(i)
    answer = 1
    cnt = 1

    if li[0] == '1':
        for i in range(len(li)-1):
            if li[i] != li[i+1]:
                answer = answer + 1
        print("#" + str(tc) + " " + str(answer))


    if li[0] == '0':
        for i in range(len(li)-1):
            if li[i] != li[i+1]:
                answer = answer + 1

        for i in range(len(li)-1):
            if i == 0:
                break
            else:
                cnt += 1

        answer = answer - cnt
        print("#" + str(tc) + " " + str(answer))