from itertools import permutations
n = int(input())
k = int(input())
lst = []
for _ in range(n):
  lst.append(input())

answer = []
for perm in permutations(lst, k):
  num = int("".join(map(str, perm)))
  if num not in answer:
    answer.append(num)

print(len(answer))
