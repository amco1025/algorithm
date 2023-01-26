num = int(input())
ans = ''
condition = ['3','6','9']

for n in range(1, num+1):
    cnt = 0
    digit = str(n)
    for d in digit:
        if d in condition:  cnt += 1

    if cnt == 0:
        ans += digit
    else: 
        for _ in range(0, cnt):
            ans += '-'
    ans += ' '

print(ans)
        
                
