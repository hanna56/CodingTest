from collections import deque

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1, n+1):
  graph[i].sort()

visited1 = []
visited2 = []

def dfs(graph, v, visited):
  visited.append(v)
  print(v, end = " ")
  for i in graph[v]:
    if i not in visited:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  queue = deque([v])
  visited2.append(v)
  print(v, end = " ")
  while queue:
    k = queue.popleft()
    for i in graph[k]:
      if i not in visited2:
        queue.append(i)
        visited2.append(i)
        print(i, end = " ")

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
