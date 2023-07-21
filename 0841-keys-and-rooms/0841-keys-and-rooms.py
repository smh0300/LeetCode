class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = list(set([x for x in rooms[0]]))
        visit = [0]
        
        while keys:
            next_key = keys.pop()
            if next_key not in visit:
                visit.append(next_key)
                new_keys = [x for x in rooms[next_key] if x not in visit]
                keys.extend(new_keys)
                
        return True if len(rooms)==len(visit) else False
        