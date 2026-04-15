class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            Time = 0
            for p in piles:
                Time += math.ceil(p/ mid)
            if Time <= h:
                r = mid
            else:
                l = mid + 1
        return l

