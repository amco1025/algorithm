from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = list()
board.append(deque(list(map(int, sys.stdin.readline().split()))))

# 정리 1 : 모든 어항 물고기 수를 확인하여 물고기가 가장 적은 어항 (중복 가능) 물고기 한 마리씩 넣기
def push_fish_to_min_bowl(graph):
    min_bowl_fish_num = min(graph[0])
    for i in range(len(graph[0])):
        if graph[0][i] == min_bowl_fish_num:
            graph[0][i] += 1


# 정리 2 : 가장 왼쪽 어항을 두 번째 어항 위로 올리기
def popleft_and_stack(graph):
    pop = graph[0].popleft()
    graph.append(deque([pop]))


# 정리 3 : 때어낸 어항 90도 회전하기
def rotate_90_clockwise(bowls):
    new_bowls = [[0] * len(bowls) for _ in range(len(bowls[0]))]
    for i in range(len(bowls[0])):
        for j in range(len(bowls)):
            new_bowls[i][j] = bowls[j][len(bowls[0]) - 1 - i]

    return new_bowls


# 정리 4 : 두 개이상 쌓인 어항 때어내기
def fly_blocks(graph):
    while True:
        if len(graph) > len(graph[0]) - len(graph[-1]):
            break

        will_fly_blocks = []
        will_fly_blocks_row = len(graph)
        will_fly_blocks_col = len(graph[-1])

        for i in range(will_fly_blocks_row):
            new_deque = deque()
            for _ in range(will_fly_blocks_col):
                new_deque.append(graph[i].popleft())
            will_fly_blocks.append(new_deque)

        graph = [graph[0]]
        rotated_blocks = rotate_90_clockwise(will_fly_blocks)
        for row in rotated_blocks:
            graph.append(deque(row))

    return graph


# 공중 부양 작업이 끝난 뒤, 어항의 물고기 수 조절.
def fix_fish_num(graph):
    dp = [[0] * len(graph[x]) for x in range(len(graph))]
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[nx]):
                    # 현재 칸이 인접 칸보다 크다면
                    if graph[x][y] > graph[nx][ny]:
                        d = (graph[x][y] - graph[nx][ny]) // 5
                        if d >= 1:
                            dp[x][y] -= d
                    # 현재 칸이 인접 칸보다 작다면
                    else:
                        d = (graph[nx][ny] - graph[x][y]) // 5
                        if d >= 1:
                            dp[x][y] += d

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] += dp[i][j]


# 다시 어항을 일렬로 놓는다
def put_bowl_in_a_row(graph):
    new_graph = deque()

    for i in range(len(graph[-1])):
        for j in range(len(graph)):
            new_graph.append(graph[j][i])

    for i in range(len(graph[-1]), len(graph[0])):
        new_graph.append(graph[0][i])

    result_list = list()
    result_list.append(new_graph)

    return result_list


# 180 도 회전
def rotate_180_clockwise(graph):
    new_graph = []

    for i in reversed(range(len(graph))):
        graph[i].reverse()
        new_graph.append(graph[i])

    return new_graph


# 다시 공중부양 작업을 한다. 이번에는 절반을 자르는데 2번 수행한다.
def fly_blocks2(graph):
    left1 = list()
    left2 = list()
    new_deque1 = deque()
    for i in range(N // 2):
        new_deque1.append(graph[0].popleft())
    left1.append(new_deque1)
    rotated_left1 = rotate_180_clockwise(left1)
    graph += rotated_left1

    for i in range(2):
        temp_deque = deque()
        for j in range(N // 4):
            temp_deque.append(graph[i].popleft())
        left2.append(temp_deque)
    rotated_left2 = rotate_180_clockwise(left2)
    graph += rotated_left2


# 물고기가 가장 많은 어항과 가장 적은 어항의 차이를 구하는 함수
def get_result(graph):
    dq = graph[0]
    result1 = max(dq) - min(dq)

    return result1


answer = 0
while True:
    result = get_result(board)
    if result <= K:
        print(answer)
        break
    push_fish_to_min_bowl(board)
    popleft_and_stack(board)
    board = fly_blocks(board)
    fix_fish_num(board)
    board = put_bowl_in_a_row(board)
    fly_blocks2(board)
    fix_fish_num(board)
    board = put_bowl_in_a_row(board)
    answer += 1
