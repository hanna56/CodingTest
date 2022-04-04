from collections import deque

def bfs(a):
  queue = deque([a])
  while queue:
    k = queue.popleft()
    for i in graph[k]:
      if not check[i]:
        check[i] = check[k] + 1
        queue.append(i)

n = int(input())
a,b = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [0]*(n+1)

for _ in range(int(input())):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

bfs(a)
print(check[b] if check[b] > 0 else -1)
