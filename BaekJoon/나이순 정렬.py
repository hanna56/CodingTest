n = int(input())
lst = []
for i in range(n):
  lst.append(list(map(str, input().split())))

lst.sort(key=lambda x: int(x[0]))

for a,b in lst:
  print(int(a),b)
