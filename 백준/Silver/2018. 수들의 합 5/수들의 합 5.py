n = int(input())
count = 1
s = 1
e = 1
sum = 1

while e != n:
    if sum == n:
        count += 1
        e += 1
        sum += e
    elif sum > n:
        sum = sum - s
        s += 1
    else:
        e += 1
        sum = sum + e

print(count)