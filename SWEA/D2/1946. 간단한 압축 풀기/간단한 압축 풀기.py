T = int(input())

for i in range(1, T+1):
    n = int(input())
    print("#"+str(i))
    answer = ""
    final = ""
    for _ in range(n):
        dic = {}
        a, b = map(str, input().split())
        dic[a] = int(b)
        for j in dic.items():
            for k in range(int(j[1])):
                answer = answer+j[0]
    
    for i in answer:
      final = final+str(i)
      if len(final) == 10:
        print(final)
        final = ""
     
    print(final)
       