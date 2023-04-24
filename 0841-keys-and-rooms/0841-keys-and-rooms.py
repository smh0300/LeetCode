class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def traversal(room):
            keys = deque()
            for _ in rooms[0]:
                keys.append(_)
            visit = [0]*len(room)
            visit[0] = 1
            while keys:
                x = keys.popleft()
                if visit[x] == 0:
                    visit[x] = 1
                    for _ in rooms[x]:
                        keys.append(_)
            return sum(visit)

        success = traversal(rooms)
        return True if success == len(rooms) else False