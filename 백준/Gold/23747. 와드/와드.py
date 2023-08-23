import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())  # 격자의 크기를 나타내는 두 정수
graph = [list(input().rstrip()) for _ in range(R)]  # 격자의 정보
Hr, Hc = map(lambda x: int(x)-1, input().rstrip().split())  # 한별이의 위치
hanbyeol_travel_record = input().rstrip()  # 한별이의 여행 기록
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for command in hanbyeol_travel_record:
    if command == 'W':
        queue = deque()
        area_seperator = graph[Hr][Hc]
        if area_seperator == '.':
            continue
        queue.append((Hr, Hc))
        graph[Hr][Hc] = '.'
        while queue:
            row, col = queue.popleft()
            for i in range(4):
                now_r, now_c = row+dr[i], col+dc[i]
                if now_r < 0 or now_r >= R or now_c < 0 or now_c >= C:
                    continue
                if graph[now_r][now_c] == area_seperator:
                    graph[now_r][now_c] = '.'
                    queue.append((now_r, now_c))
    elif command == 'U':
        Hr -= 1
    elif command == 'D':
        Hr += 1
    elif command == 'L':
        Hc -= 1
    elif command == 'R':
        Hc += 1

graph[Hr][Hc] = '.'
for i in range(4):
    now_Hr, now_Hc = Hr+dr[i], Hc+dc[i]
    if 0 <= now_Hr < R and 0 <= now_Hc < C:
        graph[now_Hr][now_Hc] = '.'

for row in range(R):
    for col in range(C):
        if graph[row][col] != '.':
            print('#', end = '')
        else:
            print('.', end = '')
    print()