T = int(input())
dic = {'0001101': 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011': 4, '0110001': 5, '0101111':6, '0111011':7,'0110111':8,'0001011':9}

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(len(arr[i])-1, -1, -1):
            if arr[i][j] == '1':
                si, sj = i, j
                break
    ans=""

    for i in range(sj-55, sj+1):
        ans+= arr[si][i]
        if len(ans) == 7:
            answer.append(dic[ans])
            ans = ""

    pw = 0
    for i in range(0, 8, 2):
        pw += answer[i]*3
    for i in range(1, 7, 2):
        pw += answer[i]
    sol = 0
    if pw > 0 and (pw + answer[7]) % 10 == 0:
        for i in answer:
            sol += i
        print("#"+str(tc)+" "+str(sol))
    else:
        print("#"+str(tc)+" "+str(0))
