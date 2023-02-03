T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    if a % (2*b + 1) == 0:
        print("#"+str(tc)+" "+str(a//(2*b+1)))
    else:
        print("#"+str(tc)+" "+str((a//(2*b + 1))+1))