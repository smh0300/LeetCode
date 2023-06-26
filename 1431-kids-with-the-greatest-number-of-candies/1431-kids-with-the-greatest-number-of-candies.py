class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)

        result=[]
        for x in candies:
            if x + extraCandies >= maxi:
                result.append(True)
            else:
                result.append(False)
        return result