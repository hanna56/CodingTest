def dfs(x,y,number):
  if len(number) == 6:
    if number not in result:
      result.append(number)
    return
  
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]

  for i in range(4):
    if x+dx[i] >= 0 and x+dx[i] < 5 and y+dy[i] >=0 and y+dy[i] < 5:
      dfs(x+dx[i], y+dy[i], number + board[x+dx[i]][y+dy[i]])

result = []
board = []
for i in range(5):
  board.append(list(map(str, input().split())))

for i in range(5):
  for j in range(5):
    dfs(i,j, board[i][j])

print(len(result))
