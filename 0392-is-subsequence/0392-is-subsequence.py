class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        if len(s)==0:
            return True
        try:
            for x in t:
                if x == s[count]:
                    count += 1
        except:
            return True if len(s)==count else False

        print(len(s), count)

        return True if len(s)==count else False