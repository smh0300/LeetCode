class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        answer = dict()

        for x in arr:
            if x not in answer:
                answer[x] = 1
            else:
                answer[x] += 1

        if len(set(answer.values())) == len(answer.values()):
            return True
        else:
            return False