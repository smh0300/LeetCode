class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = dict()
        dic2 = dict()
        for x,y in zip(s,t):
            dic1[x] = y
            dic2[y] = x

        result1 = 0
        result2 = 0

        for x,y in enumerate(t):
            if y != dic1[s[x]]:
                result1 += 1
        
        for x,y in enumerate(s):
            if y != dic2[t[x]]:
                result2 += 1
        
        if result1==0 and result2==0:
            return True
        else:
            return False