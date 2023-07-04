class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = []
        count = 0
        for x in nums:
            if x == 0:
                count += 1
            else:
                nums2.append(x)
        for x in range(count):
            nums2.append(0)
        nums[:]=nums2