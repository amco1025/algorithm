import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

N = int(input())
parent = [0] * (N+1)
for i in range(0, N+1):
    parent[i] = i

for _ in range(N-2):
    s, e = map(int, input().split())
    union(s,e)
ans = []
for i in range(1, N+1):
    if i == parent[i]:
        ans.append(i)
print(*ans)