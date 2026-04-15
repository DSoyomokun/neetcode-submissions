class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            others = nums[:i] + nums[i+1:]

            product = 1
            for val in others:
                product *= val
            res.append(product)
        return(res)


    
    
        