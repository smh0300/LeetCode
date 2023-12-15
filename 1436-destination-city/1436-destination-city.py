class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        backward=[x[1] for x in paths]
        forward=[x[0] for x in paths]
        exit = 0
        idx, city = 0, backward[0]
        while exit == 0:
            if city in forward:
                idx = forward.index(city)
                city = backward[idx]
            else:
                exit = 1
        return city