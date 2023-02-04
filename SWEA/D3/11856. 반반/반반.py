T = int(input())

for tc in range(1, T+1):
    final = 0
    a= input()
    answer = {}
    for i in a:
      i = str(i)
      answer[i] = 0
    for j in a:
      j = str(j)
      answer[j] += 1
    if len(answer) == 2:
      final = 1
    else:
      final = 0
    for k in answer.values():
      if k == 2:
        final += 1
      else:
        continue
    if final == 3:
      print("#"+str(tc)+" "+"Yes")
    else:
      print("#"+str(tc)+" "+"No")