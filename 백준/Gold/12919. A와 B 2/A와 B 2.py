import sys


# 백 트래킹을 통해 완성된 문자열로 시작 문자열을 만들 수 있는지 확인
def solution(c):
    global flag

    if len(c) == len(s):
        if c == s:
            flag = True

        return

    if c[0] == "B":
        c.reverse()
        c.pop()
        solution(c) # 백 트래킹
        c.append("B")
        c.reverse()

    if c[-1] == "A":
        c.pop()
        solution(c) # 백 트래킹
        c.append("A")


s = list(map(str, sys.stdin.readline().strip()))
t = list(map(str, sys.stdin.readline().strip()))
flag = False
solution(t)

if flag:
    print(1)
else:
    print(0)