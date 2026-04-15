class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        nums = sorted(nums)
        output_arr = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if i != j and j != k and i != k and nums[i] + nums[j] + nums[k] == 0:
                        output_arr.add((nums[i],nums[j],nums[k]))

        for element in output_arr:
            res_list.append(list(element))

        return res_list
                        