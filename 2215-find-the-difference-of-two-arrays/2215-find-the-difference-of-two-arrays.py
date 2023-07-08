class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        start=nums1[:]
        for x in start:
            while x in nums2:
                try:
                    nums2.remove(x)
                    nums1.remove(x)
                except:
                    continue
        return [nums1, nums2]