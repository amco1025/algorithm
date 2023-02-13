import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
stack = []
A = [0] * n
stack.append(n-1)

for i in range(n-2, -1, -1):
    a = i
    while len(stack) != 0:
        top = num[stack[-1]]
        if top < num[a]:
            A[stack.pop()] = a+1
        else:
            break

    stack.append(i)

print(*A)