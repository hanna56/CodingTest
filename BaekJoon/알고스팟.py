import heapq

m, n = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dist = [[0] * m for _ in range(n)]
dist[0][0] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = []
queue.append([0, (0,0)])

while queue:
  w, p = heapq.heappop(queue)
  #print(w,p)
  if p == (n-1,m-1):
    print(w)
    break
  for i in range(4):
    x = p[0] + dx[i]
    y = p[1] + dy[i]
    if 0<=x<=n-1 and 0<=y<=m-1:
      if not dist[x][y]:
        if graph[x][y] == 0:
          dist[x][y] = 1
          heapq.heappush(queue, [w, (x,y)])
        elif graph[x][y] == 1:
          dist[x][y] = 1
          heapq.heappush(queue, [w+1, (x,y)])
