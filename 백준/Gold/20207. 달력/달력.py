n = int(input())
arr = [0]*366


for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        arr[i] += 1

k = 0
con = 0
mx = 0
ans = 0

for i in range(1, 366):
    if arr[i] == 0:
        if arr[i-1] != 0:
            ans += mx*con
            con = 0
            mx = 0
        elif arr[i] == 0:
            continue

    if arr[i] != 0:
        mx = max(arr[i], mx)
        con += 1

ans += mx * con
print(ans)
