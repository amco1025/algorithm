def dfs(node):
    left_string = ''
    mid_string = node[0]
    right_string = ''
    if len(node) >= 2:
        left_string = dfs(S[int(node[1]) - 1])
    if len(node) >= 3:
        right_string = dfs(S[int(node[2]) - 1])
 
    return left_string + mid_string + right_string
 
 
for t in range(10):
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(str, input().split()))[1:])
 
    print("#{0} {1}".format(t + 1, dfs(S[0])))