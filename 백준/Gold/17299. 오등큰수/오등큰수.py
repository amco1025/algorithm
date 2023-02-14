# from collections import Counter
# from sys import stdin
# 
# n = int(stdin.readline())
# li = list(map(int, stdin.readline().split()))
# stack = Counter(li)
# stack = dict(stack)
# answer = [-1] * n
# 
# for i in range(n-1): # 현재 리스트 값을 키로 하는 딕셔너리보다 뒤에 나온 리스트 값을 키로 하는 딕셔너리
#     for j in range(i, n): # 키보다 큰 값이 있다면 출력 리스트에 그 리스트 값 저장 하고 반복문 종료
#         if stack[li[i]] < stack[li[j]]:
#             answer[i] = li[j]
#             break
# 
# print(*answer)

from collections import Counter
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
nums_count = Counter(nums)
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
            result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)
# 시간 초과 다시 풀어보기