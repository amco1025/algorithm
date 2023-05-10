import sys

N=int(sys.stdin.readline())
n = 0

while(2**(n+1)-2<N):
    n+=1


N = N -(2**n-1)


ans=""

for _ in range(n):
    if N%2==0:
        ans=ans+"4"
    else:
        ans=ans+"7"
    N=N//2

print(ans[::-1])