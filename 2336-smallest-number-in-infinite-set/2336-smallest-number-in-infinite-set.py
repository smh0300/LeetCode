class SmallestInfiniteSet:
    import heapq
    
    def __init__(self):
        self.idx = 1
        self.queue = [self.idx]
        self.history = [self.idx]

    def popSmallest(self) -> int:
        if len(self.queue) == 0:
            self.idx += 1
            heapq.heappush(self.queue, self.idx)
            self.history.append(self.idx)
            
        smallest = heapq.heappop(self.queue)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.queue:
            return
        elif num in self.history:
            heapq.heappush(self.queue, num)
        else:
            return
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)