from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer_list = []

def bfs(x,y):
  visited[x][y] = 1
  queue = deque([[x,y]])
  while queue:
    a,b = queue.popleft()
    for i in range(4):
      nx = a+dx[i]
      ny = b+dy[i]
      if 0<=nx<=n-1 and 0<=ny<=n-1 and not visited[nx][ny] and graph[nx][ny]>k:
        visited[nx][ny] = 1
        queue.append([nx,ny])

for k in range(1, 101):
  visited = [[0]*n for _ in range(n)]
  answer = 0
  dx = [-1,1,0,0]
  dy = [0,0,1,-1]

  for i in range(n):
    for j in range(n):
      if not visited[i][j] and graph[i][j] >k:
        answer+=1
        bfs(i,j)

  answer_list.append(answer)
  if answer == 0:
    break

if len(answer_list) == 1:
  print(1)
else:
  print(max(answer_list))
