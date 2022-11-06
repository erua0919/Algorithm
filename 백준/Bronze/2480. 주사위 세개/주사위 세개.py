A, B, C = map(int, input().split())

if(A == B):
  if(A == C): #A=B=C 3개
    print(10000+A*1000)
  else: #A=B 2개
    print(1000+A*100)
    

elif(A != B):
  if(A == C): #A=C 2개
    print(1000+A*100)
  elif(B == C): #B=C 2개
    print(1000+B*100)
  else:
    if(A >= B and A >= C): #A가 가장 큰 경우
      print(A*100)
    elif(B >= A and B >= C): #B가 가장 큰 경우
      print(B*100)
    else: #C가 가장 큰 경우
      print(C*100)