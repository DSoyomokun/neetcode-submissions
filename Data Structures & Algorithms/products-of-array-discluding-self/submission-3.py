class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n   # step 1: init result array

        # Prefix pass → build products to the left
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix pass → multiply products to the right
        suffix = 1
        for i in reversed(range(n)):
            res[i] *= suffix
            suffix *= nums[i]

        return res
    
        