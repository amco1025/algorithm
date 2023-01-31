T = 10

# for i in range(1, T + 1):
#   bingo = [[0]*100 for _ in range(100)]
#   answer = []
#   diagnoal_1 = 0
#   diagnoal_2 = 0
   
#   for j in range(100):
#     a = list(map(int, input().split()))
#     m = 0
#     for q in a:
#         bingo[j][m] = q
#         m += 1
        
#   for z in range(100):
#     answer.append(sum(bingo[z]))
    
#   for e in range(100):
#     column = 0
#     for r in range(100):
#         column = column + bingo[e][r]
#     answer.append(column)
                
#   for k in range(0,100):
#     diagnoal_1 = diagnoal_1 + bingo[k][k]
    
#   answer.append(diagnoal_1)
        
#   for d in range(0, 100):
#     diagnoal_2 = diagnoal_2 + bingo[d][99-d]
    
#   answer.append(diagnoal_2)
    
#   answer = max(answer)
        
#   print("#"+str(i)+" "+str(answer))

for _ in range(10) :
    T = int(input())

    array = []
    for i in range(100) :
        array.append(list(map(int, input().split())))

    # 가로줄의 합
    max_1 = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += array[i][j]
        if sum > max_1 :
            max_1 = sum

    # 세로줄의 합
    max_2 = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += array[j][i]
        if sum > max_2 :
            max_2 = sum

    # 대각선의 합
    max_3 = 0
    for i in range(100) :
        sum1 = 0 ; sum2 = 0
        sum1 += array[i][i]
        sum2 += array[i][99-i]
    if max(sum1, sum2) > max_3 :
        max_3 = max(sum1, sum2)

    print("#{} {}".format(T, max(max_1, max_2, max_3)))
        