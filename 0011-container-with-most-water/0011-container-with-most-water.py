class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max, start = 0, 0 

        def square(l, r, lst):
            length = r - l
            height = min(lst[l],lst[r])
            return length * height

        while l < r:
            max = max if square(l,r,height) < max else square(l,r,height) 

            if height[l] < height[r]:
                l += 1
            else:   
                r -= 1

            start += 1
        
        return max