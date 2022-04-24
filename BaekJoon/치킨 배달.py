from itertools import combinations

n,m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))


home = []
chicken = []
costs = []

for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      home.append([i,j])
    elif city[i][j] == 2:
      chicken.append([i,j])

for comb in combinations(chicken, m):
  cost = 0
  for house in home:
    min_cost = 1000
    for chick in comb:
      min_cost = min(min_cost, abs(chick[0]-house[0])+abs(chick[1]-house[1]))
    cost+=min_cost
  costs.append(cost)
print(min(costs))
