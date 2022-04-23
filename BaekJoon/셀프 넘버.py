nums = set(range(1,10001))
nums2 = set()
for i in nums:
  for j in str(i):
    i+=int(j)
  nums2.add(i)

answer = sorted(nums-nums2)
for k in answer:
  print(k)
