import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  s, e, c = map(int, input().split())
  graph[s].append((e,c))
  
start, end = map(int, input().split())

INF = 1e9
distance = [INF]*(n+1)

def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start))

  while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
      continue
    for node in graph[now]:
      cost = dist + node[1]
      if distance[node[0]] > cost:
        distance[node[0]] = cost
        heapq.heappush(queue, (cost, node[0]))

dijkstra(start)
print(distance[end])
