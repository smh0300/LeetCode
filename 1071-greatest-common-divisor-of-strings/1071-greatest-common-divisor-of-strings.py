class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = str1 if len(str1)<=len(str2) else str2
        len2 = str1 if len(str1)>len(str2) else str2

        def div(a,b):
            start = 1
            answer=[]
            length1 = a
            length2 = b
            for x in range(len(length1)):
                slicing = []
                for y in range(int(len(length2)/start)):
                    slicing.append(length2[y*start:start+y*start])
                if len(length2)%start != 0:
                    slicing.append(length2[-(len(length2)%start):])
                start += 1


                count = 0
                for y in slicing:
                    if length1[:x+1] ==y:
                        count += 1

                if count == len(slicing):
                    answer.append(length1[:x+1])
            return answer

        big = div(len1,len2)
        small = div(len1, len1)
        
        if len(big)==0:
            return ""
        
        for x in reversed(big):
            for y in reversed(small):
                if x==y:
                    return y
        return ""