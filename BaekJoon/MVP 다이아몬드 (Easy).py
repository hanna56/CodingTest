n = int(input())
s,g,p,d = list(map(int, input().split()))
mvp = input()

answer = 0
pred = 0
for i in range(n):
  level = mvp[i]
  if level == "B":
    answer+=s-1-pred
    pred = s-1-pred
  elif level == "S":
    answer+=g-1-pred
    pred = g-1-pred
  elif level == "G":
    answer+=p-1-pred
    pred = p-1-pred
  elif level == "P":
    answer+=d-1-pred
    pred=d-1-pred
  elif level == "D":
    answer+=d
print(answer)
