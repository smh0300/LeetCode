class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def make_dict(word):
            dic = {}    
            for x in word:
                if x not in dic:
                    dic[x] = 1
                else:
                    dic[x] += 1
            return dic


        if len(word1) != len(word2):
            print("length false")
            return False

        d1 = make_dict(word1)
        d2 = make_dict(word2)

        for x in d1.keys():
            if x not in d2:
                print("unique false")
                return False
        for x in d2.keys():
            if x not in d1:
                print("unique false")
                return False

        k1 = list(d1.values())
        k1.sort()

        k2 = list(d2.values())
        k2.sort()
        
        return True if k1==k2 else False