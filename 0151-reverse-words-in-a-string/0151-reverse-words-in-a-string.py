class Solution:
    def reverseWords(self, s: str) -> str:
        strings = []
        a = s.split(' ')
        for x,y in enumerate(reversed(a)):
            if y=='':
                continue
            else:
                strings.append(y)

        a = " ".join(strings)
        return a