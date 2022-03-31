# bfs로 풀이
from collections import deque

x = int(input())
dist = [0]*(x+1)
queue = deque([x])

while queue:
  n = queue.popleft()
  if n == 1:
    print(dist[1])
    break
  if n%3 == 0 and not dist[n//3]:
    queue.append(n//3)
    dist[n//3] =  dist[n] + 1
  if n%2 == 0 and not dist[n//2]:
    queue.append(n//2)
    dist[n//2] = dist[n] + 1
  if not dist[n-1]:
    queue.append(n-1)
    dist[n-1] = dist[n] + 1

# dp로 풀이
x = int(input())
dp = [0] * (x+1)

for i in range(2, x+1):
  dp[i] = dp[i-1]+1
  if i%3 == 0:
    dp[i] = min(dp[i], dp[i//3]+1)
  if i%2 == 0:
    dp[i] = min(dp[i], dp[i//2]+1)

print(dp[x])
