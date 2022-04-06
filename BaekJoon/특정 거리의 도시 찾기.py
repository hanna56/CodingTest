from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)

visited = [-1] * (n+1)
visited[x] = 0
queue = deque([x])

while queue:
  p = queue.popleft()
  for i in graph[p]:
    if visited[i] == -1:
      visited[i] = visited[p] + 1
      queue.append(i)

for num in range(n+1):
  if visited[num] == k:
    print(num)
if k not in visited:
  print(-1)

