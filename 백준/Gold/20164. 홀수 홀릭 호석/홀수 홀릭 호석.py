# 홀수 수 구하기

def odd(num:int):
    new_odd = 0
    while num:
        if (num%10) % 2:
            new_odd += 1
        num //= 10
    return new_odd

# 수의 자리수에 따른 연산

def sol(n:str, total:int):
    # 한자리
    if len(n) == 1:
        makes.append(total)
        return

    elif len(n) == 2:
        new_num = int(n[0]) + int(n[1])
        sol(str(new_num), total+odd(new_num))

    else:
        for i in range(1, len(n)):
            for j in range(i+1, len(n)):
                p1 = n[:i]
                p2 = n[i:j]
                p3 = n[j:]

                new_num = int(p1) + int(p2) + int(p3)
                sol(str(new_num), total + odd(new_num))
N = input()
makes = []
sol(N, odd(int(N)))
print(min(makes), max(makes))