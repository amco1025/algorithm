# 후보에 들어갈 수 있는 수
n = int(input())
# 총 학생 수
N = int(input())
# 현재 회장 후보
ans = [[-1,0,0] for _ in range(n)]
# 현재 투표 수
li = [0] * N

li = list(map(int, input().split()))

# 추천 받은 사람들의 번호를 넣으며 반복문 진행
for i in li:
    sm = 0

    # 이미 추천 명단에 있다면 추천 수 1 추가
    for j in range(n):
        if ans[j][2] == i and sm==0:
            ans[j][0] += 1
            sm = 1

    # 추천인 명단에 없다면
    if sm == 0:
        # 빈 칸이 있는지 확인
        k = 0
        for j in range(n):
            if ans[j][0] == 0:
                k += 1

        # 빈칸이 없다면
        if k == 0:
            mn = N+1
            for q in range(n):
                mn = min(mn, ans[q][0])
            c = 0
            for p in range(n):
                if ans[p][0] == mn:
                    c += 1

            if c == 1:
                for p in range(n):
                    if ans[p][0] == mn:
                        ans[p][0] = 1
                        ans[p][1] = 0
                        ans[p][2] = i

            elif c > 1:
                u = -1
                z = -1
                for m in range(n):
                    if ans[m][0] == mn and u < ans[m][1]:
                        u = ans[m][1]
                        z = m

                ans[z][0] = 1
                ans[z][1] = 0
                ans[z][2] = i

        # 빈칸이 있다면
        else:
            qw = 0
            for v in range(n):
                if ans[v][0] == 0 and qw == 0:
                    ans[v][0] = 1
                    ans[v][1] = 0
                    ans[v][2] = i
                    qw += 1

    for z in range(n):
        if ans[z][0] != 0:
            ans[z][1] += 1


answer = []

for i in range(n):
    if ans[i][2] != 0:
        answer.append(ans[i][2])

answer.sort()
print(*answer)