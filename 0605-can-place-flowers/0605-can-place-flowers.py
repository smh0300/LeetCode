class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tag = 1
        for i in flowerbed:
            tag = 0 if i else tag + 1
            if tag == 3:
                tag, n = 1, n - 1
        return n <= 1 if tag == 2 else n <= 0