class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1
        
        ans=[0] * n
        ans[0]=1
        ans[1]=1

        for x in range(2,n):
            ans[x] = ans[x-2]+ans[x-1]
        
        return ans[-1]+ans[-2]