class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for s in strs:
            arranged = ''.join(sorted(s))
            if arranged in anagram:
                anagram[arranged].append(s)
            else:
                anagram[arranged] = [s]
        return (list(anagram.values()))


        
        