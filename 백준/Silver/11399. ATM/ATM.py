N = int(input())
A = list(map(int, input().split()))
A.sort()
S = [0]*N

for i in range(N):
    S[i] = S[i-1] + A[i]
    
print(sum(S))