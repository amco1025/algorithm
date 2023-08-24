def get_score(result):
    score = []
    flag = [0] * 12
    cnt, cnt_flag = 0, 0
    for s in result:
        if s == "S":
            if cnt >= 2 and flag[cnt-2] != 0:
                score[-2] += 10
                flag[cnt-2] -= 1
            if cnt >= 1 and flag[cnt-1] != 0:
                score[-1] += 10
                flag[cnt-1] -= 1
            score.append(10)
            if cnt <= 8:
                flag[cnt] = 2
            cnt += 1
        elif s == "P":
            if cnt >= 1 and flag[cnt-1] != 0:
                score[-2] = score[-2] + 10 - score[-1]
                flag[cnt-1] -= 1
            score[-1] = 10
            if cnt != 9:
                flag[cnt] = 1
            cnt += 1
            cnt_flag = 0
        elif s == "-":
            if cnt >= 1 and flag[cnt-1] != 0:
                flag[cnt-1] -= 1
            if cnt_flag == 1:
                cnt += 1
                cnt_flag = 0
            else:
                score.append(0)
                cnt_flag = 1
        else:
            int_score = int(s)
            if cnt >= 2 and flag[cnt-2] != 0:
                score[-2] += int_score
                flag[cnt-2] -= 1
            if cnt >= 1 and flag[cnt-1] != 0:
                score[-1] += int_score
                flag[cnt-1] -= 1
            if flag[cnt] != 0:
                score[-1] += int_score
                flag[cnt] -= 1
            if cnt_flag == 1:
                score[-1] += int_score
                cnt += 1
                cnt_flag = 0
            else:
                cnt_flag = 1
                score.append(int_score)
    return sum(score)

result = input()

ans = get_score(result)
print(ans)