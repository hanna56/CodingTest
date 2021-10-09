n=int(input())
sangeun = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
sangeun.sort()

def binary_search(sangeun, start, end, target):
  while start <= end:
    mid = (start+end)//2
    if sangeun[mid] == target:
      return True
    if sangeun[mid] > target:
      end = mid-1
    else:
      start=mid+1
  return False


for i in arr:
  if binary_search(sangeun, 0, len(sangeun)-1, i) == True:
    print(1, end=" ")
  else:
    print(0, end=" ")
