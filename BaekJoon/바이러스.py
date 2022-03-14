computers = int(input())
connect = int(input())

visited = [0]* (computers+1)

graph = [[] for _ in range(computers+1)]

for _ in range(connect):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(visited, graph, v):
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      dfs(visited, graph, i)

dfs(visited, graph, 1)
print(sum(visited)-1)
