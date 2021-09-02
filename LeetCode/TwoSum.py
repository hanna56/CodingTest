class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
                  
# 해시 테이블 이용
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashtable:
                return i, hashtable[comp]
            hashtable[nums[i]] = i
