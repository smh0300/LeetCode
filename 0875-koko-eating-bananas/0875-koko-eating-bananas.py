class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            consume = 0
            for x in piles:
                consume += x//mid if x%mid==0 else (x//mid) + 1
            if consume > h:
                l = mid + 1
            else:
                r = mid

        return l