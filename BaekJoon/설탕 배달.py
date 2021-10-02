N = int(input())
answer = 0

if N%5==0:
  print(N//5)
else:
  answer = 0
  while N>=5:
    if (N-3) % 5 == 0:
      answer+=N//5+1
      N = (N-3) % 5
    else:
      N-=3
      answer+=1
  print(answer+N//3) if N%3==0 else print(-1)

  
   
