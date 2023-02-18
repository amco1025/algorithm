n = int(input())


def per(level, count):
    global result
    if level == N:
        result = max(result, count)

    else:
        for i in range(N):
            if not visited[i] and count * arr[level][i] * 0.01 > result:
                visited[i] = 1
                per(level + 1, count * arr[level][i] * 0.01)
                visited[i] = 0


for tc in range(1, n + 1):
    N = int(input())
    visited = [0] * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    per(0, 1)
    print("#%d %f" % (tc, result * 100))


# def DFS(i, n, ans, v, N):
#     global mn
# 
#     if ans <= mn:
#         return
#     if n == N:
#         if ans > mn:
#             mn = ans
# 
#     else:
#         for j in range(N):
#             if v[j] == 0:
#                 v[j] = 1
#                 DFS(i + 1, n + 1, ans * arr[i][j] / 100, v, N)
#                 v[j] = 0
#     return mn
# 
# 
# T = int(input())
# 
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     n = 0
#     v = [0] * N
#     mn = 0
#     ans = 1
# 
#     for j in range(N):
#         DFS(0, n, ans, v, N)
#     mn = mn * 100
#     mn = float(round(mn, 6))
# 
#     print("#" + str(tc) + " " + str(mn))
# 시간초과 다시