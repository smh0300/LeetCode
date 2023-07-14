from collections import deque

class RecentCounter:

    queue = deque()
    def __init__(self):
        self.my_deque = deque()

    def ping(self, t: int) -> int:
        self.my_deque.append(t)
        while self.my_deque[0] < t-3000:
            self.my_deque.popleft()
        return len(self.my_deque)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)