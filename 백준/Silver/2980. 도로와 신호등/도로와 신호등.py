N, L = map(int, input().split())
# 시간
cnt = 0
# 거리
ln = 0
for _ in range(N):
    D, R, G = map(int, input().split())
    li = [0] *(R+G)
    for i in range(R):
        li[i] = R-i
    if ln < D:
        cnt += D-ln
        ln = D
    if ln == D:
        s = cnt%(R+G)
        cnt += li[s]

cnt += L-ln
print(cnt)