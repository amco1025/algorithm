def isPal(arr, M):
    for lst in arr:
        for i in range(N-M+1):
            if lst[i:i+M] == lst[i:i+M][::-1]:
                return True
    return False

T = 10
for tc in range(1, T+1):
    n = int(input())
    N = 100
    arr = [input() for _ in range(N)]
    arr_t = list(zip(*arr))
    for M in range(N, 1, -1):
        if isPal(arr, M) or isPal(arr_t, M):
            break
    else:
        M =1
    print("#"+str(tc)+" "+str(M))