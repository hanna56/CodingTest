from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b]+=1

def topology_sort():
  semester = [0 for _ in range(n+1)]
  q = deque()

  for i in range(1, n+1):
    if indegree[i] == 0:
      q.append(i)
      semester[i] = 1

  while q:
    a = q.popleft()
    for i in graph[a]:
      indegree[i]-=1
      semester[i]=semester[a]+1
      if indegree[i] == 0:
        q.append(i)

  for i in range(1, n+1):
    print(semester[i], end = " ")
  
topology_sort()
