class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n ==0:
            return 0
        elif n== 1:
            return 1
        elif n== 2:
            return 1
        
        answer = [0]*(n+1)
        answer[0] = 0
        answer[1] = 1
        answer[2] = 1

        for x in range(3,n+1):
            answer[x] = answer[x-3] + answer[x-2] + answer[x-1]
        
        return answer[-1]