import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [True for _ in range(n+1)]

answer=[]

for i in range(2, n+1):
  if arr[i] == True:
    answer.append(i)
    j=2
    while i*j <= n:
      if arr[i*j] == True:
        arr[i*j] = False
        answer.append(i*j)
      j+=1

print(answer[k-1])
