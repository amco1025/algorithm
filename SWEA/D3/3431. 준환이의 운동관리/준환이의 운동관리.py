T = int(input())

for tc in range(1, T+1):
    A, B, C  = map(int, input().split())
    if C < A:
        print("#"+str(tc)+" "+str(A-C))
    elif C >= A and C <= B:
        print("#"+str(tc)+" "+str(0))
    else:
        print("#"+str(tc)+" "+str(-1))