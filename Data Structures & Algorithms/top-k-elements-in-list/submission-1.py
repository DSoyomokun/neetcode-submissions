class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        res = sorted(count.items(), key=lambda number: number[1], reverse=True)
        final = []
        for n in range(k):
            final.append(res[n][0])
        return (final)
            
        