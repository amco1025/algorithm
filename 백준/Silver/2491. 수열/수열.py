import sys
input  = sys.stdin.readline
del input

n = int(input())
num = list(map(int,input().split()))

#dp: i번째까지 왔을때 수열의 최대 길이-증가할때/감소할때 
d = [[1]*n for _ in range(2)]

for i in range(1,n):
    if num[i-1]<=num[i]: #증가할경우
        d[0][i] = d[0][i-1]+1
        
    if num[i-1]>=num[i]: #감소할경우
        d[1][i] = d[1][i-1]+1
        
print(max(map(max,d)))