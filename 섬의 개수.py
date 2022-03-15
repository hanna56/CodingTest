import sys
sys.setrecursionlimit(1000000)

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def dfs(k,v):
  if 0<=k<h and 0<=v<w:
    if graph[k][v] == 1:
      graph[k][v] = 2
      for i in range(8):
        dfs(k+dx[i], v+dy[i])

while True:
  w,h = map(int, input().split())
  if w == 0 and h == 0:
    break

  graph= []
  count = 0

  for _ in range(h):
    graph.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        dfs(i,j)
        count+=1

  print(count)
