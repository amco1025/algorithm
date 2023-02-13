import sys

n, p = map(int, sys.stdin.readline().split())
stack = [[0] for _ in range(7)]
cnt = 0

# n번 반복하며 내어야 할 소리의 n,p 입력
for i in range(n):
    line_num, plat_num = map(int, sys.stdin.readline().split())

# 주어진 줄의 더 높은 프렛을 누르고 있는 경우, 손가락을 하나씩 뗀다.
    while stack[line_num][-1] > plat_num:
        stack[line_num].pop()
        cnt += 1

# 눌러야 할 줄의 프랫보다 큰 프랫을 다 제거 후 내야할 음이 이미 누르고 있는 프랫인 경우 패스
    if stack[line_num][-1] == plat_num:
        continue

#눌러야 할 줄의 프랫보다 큰 프랫을 다 제거 후 내어야 할 주어진 줄의 프랫을 누른다.
    stack[line_num].append(plat_num)
    cnt += 1

print(cnt)