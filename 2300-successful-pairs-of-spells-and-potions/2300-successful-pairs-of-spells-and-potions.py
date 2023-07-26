class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        res = []
        for s in spells:
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * s < success:
                    left = mid + 1
                else:
                    right = mid
            res.append(N - left)
        return res