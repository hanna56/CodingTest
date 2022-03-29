import sys 
sys.setrecursionlimit(10000)

def dfs(x,y,graph):
  dx=[-1,1,0,0]
  dy=[0,0,1,-1]

  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx >=0 and ny>=0 and nx <m and ny<n:
      if graph[ny][nx] == 1:
        graph[ny][nx] = 0
        dfs(nx, ny, graph)

t = int(input())
answer = []
for _ in range(t):
  count = 0
  m,n,k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1
  
  for a in range(m):
    for b in range(n):
      if graph[b][a] == 1:
        dfs(a,b,graph)
        count+=1
  answer.append(count)

for ans in answer:
  print(ans)
