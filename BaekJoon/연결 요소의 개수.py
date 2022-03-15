import sys
sys.setrecursionlimit(10000)

def dfs(v):
  visited[v] = True
  for j in graph[v]:
    if visited[j]==0:
      dfs(j)

n,m = map(int, input().split())
graph=[[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
    
for i in range(1, n+1):
  if visited[i]==0:
    dfs(i)
    count+=1  

print(count)
