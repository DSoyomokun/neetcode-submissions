class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        longest_seq = 0
        s = set(nums)
        for num in s:
            if (num - 1) not in s:
                count = 1
                while (num + 1) in s:
                    count += 1
                    num += 1
                longest_seq = max(count, longest_seq)
        return (longest_seq)
                
                

                    
                      


            


        
        