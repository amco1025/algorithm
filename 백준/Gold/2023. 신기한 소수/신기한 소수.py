import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
del input

N = int(input())

def isPrime(num):
  for i in range(2, int(num/ 2 + 1)):
    if num % i ==0:
      return False
  return True

def DFS(numbers):
  if len(str(numbers)) == N:
    print(numbers)
  else:
    for i in range(1, 10):
      if i % 2 == 0:
        continue
      if isPrime(numbers * 10 + i):
        DFS(numbers*10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)