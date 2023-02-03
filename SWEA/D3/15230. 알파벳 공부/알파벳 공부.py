T = int(input()) # 테스트 케이스 수 입력

for tc in range(1, T+1): # 반복
  a = str(input()) # 문자열 입력
  answer = []  #연속한 개수 저장할 리스트 생성
  li = [] # 입력한 문자를 리스트로 저장할 리스트 생성
  for i in a:  # 입력한 문자열을 리스트로 만들기
    li.append(i)     
  b = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j', '10':'k', '11':'l', '12':'m', '13':'n', '14':'o', '15':'p', '16':'q', '17':'r', '18':'s', '19':'t', '20':'u', '21':'v', '22':'w', '23':'x', '24':'y', '25':'z'} # 알파벳 딕셔너리
  cnt = 0   
  for k in range(len(li)): #입력한 문자열 길이 만큼 반복
    k = str(k) 
    if b[k] == li[cnt]: # 알파벳 딕셔너리에 순서에 저장된 값과 입력한 리스트 순서에 저장된 값이 같다면
      answer.append(1) # answer1 추가
      cnt += 1
    else:
      break
    

  answer = len(answer) # answer길이가 답
            
  print("#"+str(tc)+" "+str(answer))

# 너무 지저분하게 풀었다 다음에 다시 풀어보기