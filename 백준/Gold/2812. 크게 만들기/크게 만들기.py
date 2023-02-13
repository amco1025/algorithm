import sys
input = sys.stdin.readline

# 자릿수와 빼야할 수의 개수 입력
n, k = map(int, input().split())
numbers = input().rstrip() # 주어진 수 입력
stack = [] # 출력할 수를 저장할 스택 생성

for i in numbers: # i에 주어진 수 넣으며 반복
    while stack and stack[-1] < i and k > 0: # 만들어 질 수는 있는 최대 자리수가 n-k를 유지하며 전 수보다 들어온 수가 클 시 앞에 수 제거
        stack.pop()
        k -= 1 # 제거 후 빼야 할 수의 개수 -1
    stack.append(i)
if k > 0: # k개를 빼야 하는데 뒤에수가 앞에 수 보다 큰 경우가 k횟수 보다 적어 못 뻈을시 앞부터 정해진 길이까지 출력
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))