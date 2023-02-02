T = int(input())

for tc in range(1, T+1):
  n = int(input())
  a = input()
  li = []
  for i in range(n):
    li.append(int(a) % 10)
    a = int(a) // 10
    cnt = 0
    answer =[]
    for j in li:
      if j == 1:
        cnt += 1
      else:
        answer.append(cnt)
        cnt = 0
  answer = max(answer)
  print("#"+str(tc)+" "+str(answer))