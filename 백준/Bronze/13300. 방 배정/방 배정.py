n, k = map(int, input().split())
st = [[0]*2 for _ in range(6)] 

for _ in range(n):
    s, y = map(int, input().split())
    st[y-1][s-1] += 1


room_num=0
for a in range(6):
    for b in range(2):
        if(st[a][b]%k == 0):
            room_num += st[a][b]/k
        else:
            room_num += st[a][b]//k + 1
            
print(int(room_num))