import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num1 in enumerate(numbers):
            num2 = target - num1
            if num2 in numbers:
                return [idx+1, bisect.bisect_right(numbers, num2)]
        
