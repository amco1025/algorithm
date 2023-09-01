import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    # 마지막에 modulo를 진행한 결과가 0이 나왔을 때, a에 b값을 넣어주고 끝나기 때문에 a를 return한다.
    return a

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

answer = 1
for i in range(len(list1)):
    for j in range(len(list2)):
        gcd_result = gcd(list1[i], list2[j])
        answer *= gcd_result
        list1[i] //= gcd_result
        list2[j] //= gcd_result

print(str(answer)[-9:])
