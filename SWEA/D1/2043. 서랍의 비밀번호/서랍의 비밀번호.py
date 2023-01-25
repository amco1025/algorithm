P, K = map(int, input().split()) # 비밀 번호와 주어진 수를 P와K에 할당.

if P > K:
    print(P - K + 1)
elif P == K:
    print(1)
else:
    print(999 - K + P + 1)
