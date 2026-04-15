class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashhy = set()
        for cock in nums:
            if cock in hashhy:
                return True
            hashhy.add(cock)
        return False
        
    
        
