class Solution:
    def tribonacci(self, n: int) -> int:
        from collections import deque
        fibo = deque([0,1,1])
        
        if n<3:
            return fibo[n]
        
        for x in range(3,n):
            print(fibo)
            cur_sum = sum(fibo)
            fibo.popleft()
            fibo.append(cur_sum)
        return sum(fibo)
            
            