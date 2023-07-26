class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums.insert(0,-float('inf'))
        nums.insert(len(nums),-float('inf'))
        
        print(nums)
        
        for x in range(len(nums)-1):
            if nums[x] < nums[x + 1] and nums[x + 1] > nums[x + 2]:
                return x
            