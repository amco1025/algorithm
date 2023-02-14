T = int(input())
for tc in range(1, T+1):
    sticks = list(map(str, input()))
    stack = []
    cnt = 0
    for i in range(len(sticks)):
        if sticks[i] =="(":
            stack.append("(")
        elif sticks[i] == ")":
            if sticks[i-1] == "(":
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt+= 1
    print("#"+str(tc)+" "+str(cnt))