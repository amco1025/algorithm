T = int(input()) # 테스트 케이스 입력

for tc in range(1, T+1): # 테스트 케이스 수 만큼 반복문 진행
    answer = 1*2*3*4*5*6*7*8*9 # 스도쿠가 맞을라면 기준이 되는 수 9개의 곱이 1부터 9까지 곱한 것 이어야 한다.
    sdo = [[0]*9 for _ in range(9)] # 문제에서 주어진 수도쿠 판 입력
    final = 1
    for j in range(9):
        a = list(map(int, input().split()))
        m = 0
        for q in a:
            sdo[j][m] = q
            m += 1
    
    for i in range(9): # 1~9행 모두 각 행의 곱이 answer인지 확인
      check = 1 # 아니라면 출력 값을 0으로 바꾸고 같다면 계속하여 반복문 진행
      for j in range(9):
        check = check * sdo[i][j]
    	    
      if check == answer:
        continue
      else:
        final = 0
            
    for e in range(9): # 세로
      col = 1
      for r in range(9):
        col = col * sdo[r][e]
      if col == answer:
        continue
      else:
        final = 0
            
    for u in range(0, 6, 3): # 각 1~9번 방
      for h in range(0, 6, 3):
        each = 1
        for t in range(3):
          for y in range(3):
            each = each * sdo[h + t][u + y]
          
        if each == answer:
          continue

        else:
          final = 0
                
    print("#"+str(tc)+" "+str(final)) # 조건에 맞추어 출력
    
    
    # 다른 방법이 생각이 안나 반복문을 너무 많이 사용했다. 나중에 다시 풀어보기