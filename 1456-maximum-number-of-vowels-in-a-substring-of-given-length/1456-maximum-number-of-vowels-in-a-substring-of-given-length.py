class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def counting(lst):
            count = 0
            for x in vl:
                count += lst.count(x)
            return count

        vl = ['a','e','i','o','u']
        slide = s[0:k]
        max = now = counting(slide)

        for x in range(k,len(s)):
            if slide[0] in vl:
                now -= 1
            if s[x] in vl:
                now += 1
            slide = slide[1:]
            slide = slide + s[x]

            max = max if max > now else now
        return max