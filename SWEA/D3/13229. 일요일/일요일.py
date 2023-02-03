T = int(input())

for tc in range(1, T+1):
    a = {'MON' : 1, 'TUE' : 2, 'WED' : 3, 'THU' : 4, 'FRI' : 5, 'SAT' : 6, 'SUN' : 7}
    b = input()
    if b == 'SUN':
         print("#"+str(tc)+" "+"7")
    else:
        answer = 7 - a[b]
        print("#"+str(tc)+" "+str(answer))
