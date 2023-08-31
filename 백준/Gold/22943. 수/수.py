import sys
from itertools import permutations

input = sys.stdin.readline

k, m = map(int, input().split())
is_prime = [True] * (10 ** k)

iter_range = int((10 ** k) ** 0.5)

for i in range(2, iter_range + 1):
    if is_prime[i]:
        for j in range(i + i, 10 ** k, i):
            is_prime[j] = False

count = 0
# 나타날 수 있는 모든 수
for perm in permutations(range(10), k):
    # 첫자리 0이면 제외
    if perm[0] == 0:
        continue
    # 수로 변환
    num = int(''.join(list(map(str, perm))))
    temp = num
    # m으로 나눠질 때 까지 나누기
    while temp % m == 0:
        temp = temp // m

    for i in range(2, int(temp ** 0.5) + 1):
        if temp % i == 0:
            # 소수의 곱으로 나타나짐
            if is_prime[i] and is_prime[temp // i]:
                for j in range(2, num // 2):
                    # 소수의 합으로 보여짐
                    if is_prime[j] and is_prime[num - j]:
                        count += 1
                        break
                break
            break

print(count)

