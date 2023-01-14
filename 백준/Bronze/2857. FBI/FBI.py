fbi = []

for i in range(1,6):
    a = input()
    if "FBI" in a:
        fbi.append(i)
        
if len(fbi) > 0:
    print(*fbi)
else:
    print("HE GOT AWAY!")