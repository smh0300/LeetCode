class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = now = 0
        for x in gain:
            now += x
            max = max if max > now else now
        return max