import sys 
input = sys.stdin.readline
del input 

N = int(input())
M = int(input())

A = list(map(int, input().split()))
A.sort()
i = 0
j = N - 1
cnt = 0 

while i < j:
    if A[i] + A[j] < M:
        i = i + 1
    elif A[i] + A[j] > M:
        j = j -1
    else:
        cnt += 1
        i = i + 1
        j = j - 1

print(cnt)
        