# n = int(input())
# dic = {}
# 
# for i in range(n):
#     a, b = map(int, input().split())
#     dic[i] = [a, b]
# 
# ans = [0] * n
# 
# for i in range(n):
#     sm = 0
#     k = dic[i][0]
#     m = dic[i][1]
#     for j in dic.keys():
#         if dic[j][0] != k and m > dic[j][1]:
#             sm += dic[j][1]
# 
#     ans[i] = sm
# 
# for i in ans:
#     print(i)

import sys

n = int(input())
INF = 200000
balls = []

for i in range(n):
    color, size = map(int, sys.stdin.readline().split())
    balls.append((size, color, i))
    # 공의 size, color, input 순서(player)에 대한 정보를 넣는다

balls.sort()
color_count = [0] * (INF + 1)
total = 0
j = 0
ans = [0] * (n + 1)
for i in range(n):
    while balls[j][0] < balls[i][0]:  # 문제의 제한조건에서 player가 잡을 수 있는 전제 조건 중 하나인
        # 나의 공보다 사이즈가 작아야 잡을 수 있다의 조건을 충족시켜주기 위한 부분
        color_count[balls[j][1]] += balls[j][0]
        total += balls[j][0]
        j += 1
    ans[balls[i][2]] = total - color_count[balls[i][1]]  # 누적합 계산
# 나의 공보다 작은 공들의 크기 총합에서 나와 색깔이 같은
# 공들의 합을 빼준다
# 문제의 제한 조건 중 하나인 색깔이 다른 공만 잡을 수 있다
# 여기까지 완료해 주면 문제의 두가지 제한조건이 완성

for i in range(n):
    print(ans[i])
