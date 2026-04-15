class Solution:
    def twoSum(self, nums: List[int], target: int,) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in memo:
                return [memo[difference], i]
            memo[num] = i
        

        