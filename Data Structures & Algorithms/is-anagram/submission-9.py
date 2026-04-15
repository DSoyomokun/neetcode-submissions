class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = {}
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1

        count2 = {}
        for char in t:
            if char not in count2:
                count2[char] = 0
            count2[char] += 1

        if len(t)!= len(s):
            return False 
        else:
            return count == count2
            
            

