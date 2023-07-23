class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from collections import defaultdict,deque

        answer = dict()
        for x in nums:
            if x not in answer:
                answer[x] = 1
            else:
                answer[x] += 1

        nums = list(set(nums))
        queue = sorted(deque(nums[:k]),reverse=True)
        length = len(queue)
        for x,y in enumerate(nums[k:]):
            if y > queue[-1]:
                l,r = 0, k-1
                mid = int(k/2)

                while l <= r:
                    mid = (r + l)//2
                    if queue[mid] == y:
                        break
                    elif queue[mid] > y:
                        l = mid + 1
                    elif queue[mid] < y:
                        r = mid - 1
                queue.insert(mid, y)
                queue.pop()

        sum, idx, real = 0, 0, 0
        while sum < k:

            sum += answer[queue[idx]]
            real = queue[idx]
            idx += 1


        return real