T = int(input())
 
for tc in range(1, T+1):
    T = input()
    S = []
    D = []
    H = []
    C = []
    answer = 1
    Sn = 13
    Dn = 13
    Hn = 13
    Cn = 13
 
    for i in range(0, len(T), 3):
        if T[i] == 'S':
            ans = ''
            ans = ans+T[i+1]
            ans = ans+T[i+2]
            if ans in S:
                answer = 0
                S.append(ans)
            else:
                S.append(ans)
 
        if T[i] == 'D':
            ans = ''
            ans = ans+T[i+1]
            ans = ans+T[i+2]
            if ans in D:
                answer = 0
                D.append(ans)
            else:
                D.append(ans)
 
        if T[i] == 'H':
            ans = ''
            ans = ans+T[i+1]
            ans = ans+T[i+2]
            if ans in H:
                answer = 0
                H.append(ans)
            else:
                H.append(ans)
 
        if T[i] == 'C':
            ans = ''
            ans = ans+T[i+1]
            ans = ans+T[i+2]
            if ans in C:
                ans = 0
                C.append(ans)
            else:
                C.append(ans)
 
    Sn = Sn - len(S)
    Dn = Dn - len(D)
    Hn = Hn - len(H)
    Cn = Cn - len(C)
 
    if answer == 0:
        print("#"+str(tc)+" "+'ERROR')
    else:
        print("#"+str(tc)+" "+str(Sn)+" "+str(Dn)+" "+str(Hn)+" "+str(Cn))
