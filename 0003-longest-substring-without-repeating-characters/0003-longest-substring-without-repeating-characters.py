class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        answer = 0
        queue = deque()

        for x in s:
            if x not in queue:
                queue.append(x)
            else:
                idx = queue.index(x)
                for _ in range(idx + 1):
                    queue.popleft()
                queue.append(x)
            answer=max(answer,len(queue))
        return answer