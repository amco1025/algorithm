T = int(input())
for tc in range(1, T+1):
    n = int(input())
    if n == 1:
        print("#"+str(tc)+" "+"Bob")
    elif n % 2 == 0:
        print("#"+str(tc)+" "+"Alice")
    else:
        print("#"+str(tc)+" "+"Bob")
