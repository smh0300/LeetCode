class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = [0 for _ in range(len(nums) + 1)]
        r = [0 for _ in range(len(nums) + 1)]
        for x,y in enumerate(nums):
            l[x+1] = l[x] + y
            r[len(nums)-x-1] = r[len(nums)-x] + nums[len(nums)-x-1]

        for y,x in enumerate(range(len(nums))):
            if l[x] == r[x+1]:
                return y
        return -1