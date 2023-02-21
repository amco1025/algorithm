T = 10

for tc in range(1, T+1):
    a, b = map(str, input().split())
    b = list(b)
    li = []
    ans = ""

    for i in b:
        if li and i == li[-1]:
            li.pop()
        else:
            li.append(i)

    for i in li:
        ans=ans+i

    print("#"+str(tc)+" "+ans)