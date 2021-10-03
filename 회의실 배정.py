n=int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst = sorted(lst, key = lambda x: (x[1], x[0]))

answer = 1
curr = 0
for i in range(1, len(lst)):
  if lst[curr][1] <= lst[i][0]:
    answer+=1
    curr = i

print(answer)
