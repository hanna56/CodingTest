from collections import deque

n, k = map(int, input().split())
queue = deque([n])

MAX = 200000
dist = [0] * MAX

while queue:
  num = queue.popleft()
  if num == k:
    break
  for i in (num-1, num+1, 2*num):
    if 0<=i<MAX and dist[i]==0:
      dist[i] = dist[num] + 1
      queue.append(i)

print(dist[k])
