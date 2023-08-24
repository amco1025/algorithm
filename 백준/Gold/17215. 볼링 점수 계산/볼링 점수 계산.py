def bowling_score(s):
    rolls = []
    for char in s:
        if char == 'S':
            rolls.append(10)
        elif char == 'P':
            rolls.append(10 - rolls[-1])
        elif char == '-':
            rolls.append(0)
        else:
            rolls.append(int(char))

    score = 0
    frame_idx = 0
    for frame in range(10):  # 10 프레임만 점수 계산
        if rolls[frame_idx] == 10:  # 스트라이크
            score += 10 + rolls[frame_idx + 1] + rolls[frame_idx + 2]
            frame_idx += 1
        elif rolls[frame_idx] + rolls[frame_idx + 1] == 10:  # 스페어
            score += 10 + rolls[frame_idx + 2]
            frame_idx += 2
        else:  # 일반 점수
            score += rolls[frame_idx] + rolls[frame_idx + 1]
            frame_idx += 2
    return score

li = input()
print(bowling_score(li))