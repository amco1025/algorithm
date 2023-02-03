T = int(input())
final = []
for tc in range(1, T+1):
    A, B, C, D = list(map(int, input().split()))
    a = [0] * 101
    b = [0] * 101
    answer = 0
    for i in range(A+1, B+1):
        a[i] = 1
    for j in range(C+1, D+1):
        b[j] = 1
    for p in range(101):
        if a[p] == 1 & b[p] == 1:
            answer += 1
        else:
            continue
    final.append(answer)
for k in range(1, T+1):
    print("#"+str(k)+" "+str(final[k-1]))
    