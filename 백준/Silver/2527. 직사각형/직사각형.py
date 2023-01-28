for i in range(4): # 문제에 맞추어 4번 반복
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())  # 2 직사각형의 양쪽 모서리 입력
 
    
    xl = max(x1, x2) # 차이 값을 구하기 위하여 x를 비교하여 최대 p를 비교하여 최소 y를 비교하여 최대 y를 비교하여 최소를 구한다.
    xr = min(p1, p2)
    yb = max(y1, y2)
    yt = min(q1, q2)

   
    xdiff = xr - xl # x_diff에 최소 - 최대 저장 최소는 p끼리 최대는 x끼리
    ydiff = yt - yb # y_diff에 최소 - 최대 저장 최소는 q끼리 최대는 y끼리
    
  
    if xdiff > 0 and ydiff > 0: # 차가 둘다 0보다 크다면
        print('a')
    elif xdiff < 0 or ydiff < 0: # 차가 둘다 0보다 작다면
        print('d') 
    elif xdiff == 0 and ydiff == 0: # 차가 둘다 0이라면
        print('c')
    else:
        print('b')