N, money = map(int, input().split())
lst = [int(input()) for _ in range(N)]

lst.reverse()

answer = 0

for i in range(N):
  if money >= lst[i]:
    answer+=money//lst[i]
    money %= lst[i]
  if money == 0:
    print(answer)
    break
