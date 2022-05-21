from collections import deque

n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
for _ in range(k):
  a,b = map(int, input().split())
  arr[a-1][b-1] = 1
L = int(input())
times = {}
for _ in range(L):
  x,c = input().split()
  times[int(x)] = c
    
def change(d, c):
  if c == "L":
    d = (d-1)%4
  elif c == "D":
    d = (d+1)%4
  return d

# 상 우 하 좌
dy=[-1,0,1,0]
dx=[0,1,0,-1]

direction = 1
time = 1
y,x = 0,0
visited = deque([[y,x]])
arr[y][x] = 2
while True:
  y,x = y+dy[direction],x+dx[direction]
  if 0<=y<n and 0<=x<n and arr[y][x] !=2:
    if not arr[y][x] == 1:
      temp_y, temp_x = visited.popleft()
      arr[temp_y][temp_x] = 0
    arr[y][x] = 2
    visited.append([y,x])
    if time in times.keys():
      direction = change(direction, times[time])
    time+=1
  else:
    print(time)
    break
