from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dx = [1,0,-1,0]
dy = [0, 1, 0, -1]

queue = deque([[0,0]])
while queue:
  x,y = queue.popleft()
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx<n and nx>=0 and ny<m and ny>=0:
      if graph[nx][ny] == 1:
        queue.append([nx,ny])
        graph[nx][ny] = graph[x][y] + 1

print(graph[n-1][m-1])
