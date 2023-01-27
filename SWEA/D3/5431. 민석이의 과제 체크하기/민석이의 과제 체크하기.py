T = int(input())
 
for tc in range(1,1+T):
    n,k = map(int,input().split())
    submitted = list(map(int,input().split()))
    no_submitted = []
 
    for q in range(1,n+1):
        if q not in submitted:
            no_submitted.append(q)
 
    print('#{}'.format(tc),*no_submitted)
		
# 어려웠던 부분
# 리스트로 저장된 값을 문제가 원하는 것 처럼 출력 하지 못하였다.
# *사용하기
      
                  
    