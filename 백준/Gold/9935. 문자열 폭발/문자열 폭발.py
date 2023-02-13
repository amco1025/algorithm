import sys
input = sys.stdin.readline

n = sys.stdin.readline().rstrip()
m = sys.stdin.readline().rstrip()

answer = []
N = len(m)

for i in range(len(n)):
    answer.append(n[i])
    if answer[-N:] == list(m):
        for _ in range(N):
            answer.pop()

if answer:
    print(''.join(answer))
else:
    print('FRULA')