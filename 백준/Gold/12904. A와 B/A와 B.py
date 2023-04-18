li = list(map(str, input()))
ans = list(map(str, input()))

# 주어진 답을 하나씩 빼며 되돌리기

while len(li) != len(ans):
    if ans[-1] == 'B':
        ans.pop()
        ans = ans[::-1]
    else:
        ans.pop()

if li == ans:
    print(1)
else:
    print(0)

