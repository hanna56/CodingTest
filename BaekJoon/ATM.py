n = int(input())
atm= list(map(int, input().split()))
atm.sort()
result = 0
answer = 0

for i in range(len(atm)):
  result+=atm[i]
  answer+=result

print(answer)
