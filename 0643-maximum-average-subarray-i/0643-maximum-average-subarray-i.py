class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = now = sum(nums[:k])
        for x in range(k,len(nums)):
            now = now - nums[x-k] + nums[x]
            best = best if now < best else now
        return best/k