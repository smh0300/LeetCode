class Solution:
    def removeStars(self, s: str) -> str:
        answer = ""
        for x in s:
            if x != "*":
                answer = answer + x
            else:
                answer = answer[:-1]
        return answer