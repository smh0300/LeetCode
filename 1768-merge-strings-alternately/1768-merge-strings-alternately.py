class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = word1 if (len(word1)<=len(word2)) else word2
        length2 = word1 if (len(word1)>len(word2)) else word2

        word3 = ""

        for x in range(len(length1)):
            word3 = word3 + word1[x] + word2[x]

        word3 = word3 + length2[len(length1):]
        
        return word3