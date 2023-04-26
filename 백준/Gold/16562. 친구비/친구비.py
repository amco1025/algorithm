def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

n, m, k = map(int, input().split())
li = list(map(int, input().split()))
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)

for i in range(len(parent)):
    find(i)

parent.pop(0)

ans = {}

for i in range(n):
    if parent[i] in ans:
        ans[parent[i]].append(li[i])
    else:
        ans[parent[i]] = []
        ans[parent[i]].append(li[i])

sm = 0

for i in ans.keys():
    sm += min(ans[i])

if sm > k:
    print("Oh no")
else:
    print(sm)