n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

num = 0
ans = []

def dfs(x,y):
  global num
  dx = [-1,1,0,0]
  dy = [0,0,1,-1]

  if x<0 or x>=n or y<0 or y>=n:
    return False
  if graph[x][y] == 1:
    num+=1
    graph[x][y] = 0
    for i in range(4):
      dfs(x+dx[i],y+dy[i])
    return True

for i in range(n):
  for j in range(n):
    if dfs(i,j) == True:
      ans.append(num)
      num = 0

print(len(ans))
for i in sorted(ans):
  print(i)
