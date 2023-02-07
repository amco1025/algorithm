T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    answer = (a+b)%24
    
    print("#"+str(tc)+" "+str(answer))