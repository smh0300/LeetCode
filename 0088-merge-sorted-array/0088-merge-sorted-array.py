class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        answer=[]
        nums1_ptr, nums2_ptr = 0, 0
        while nums1_ptr != m and nums2_ptr != n:
            if nums1[nums1_ptr] > nums2[nums2_ptr]:
                answer.append(nums2[nums2_ptr])
                nums2_ptr += 1        
            elif nums1[nums1_ptr] < nums2[nums2_ptr]:
                answer.append(nums1[nums1_ptr])
                nums1_ptr += 1
            else:
                answer.append(nums1[nums1_ptr])
                answer.append(nums2[nums2_ptr])
                nums1_ptr += 1
                nums2_ptr += 1
        if nums1_ptr !=m:
            for x in nums1[nums1_ptr:m]:
                answer.append(x)
        elif nums2_ptr != n:
            for x in nums2[nums2_ptr:n]:
                answer.append(x)

        for i in range(len(answer)):
            nums1[i]=answer[i]