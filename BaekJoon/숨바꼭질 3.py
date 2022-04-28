import heapq

n, k = map(int, input().split())
visited = [0] * 100001
visited[n] = True

queue = []
queue.append([0, n])

while queue:
  t,q = heapq.heappop(queue)
  if q == k:
    print(t)
    break
  if 2*q < 100001 and not visited[2*q]:
    visited[2*q] = 1
    heapq.heappush(queue, [t, 2*q])
  for i in (q-1,q+1):
    if i >=0 and i<100001 and not visited[i]:
      visited[i] = 1
      heapq.heappush(queue, [t+1, i])
