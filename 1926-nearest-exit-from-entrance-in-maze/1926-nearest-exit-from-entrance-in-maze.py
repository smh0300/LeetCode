class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        h, w = len(maze), len(maze[0])

        from collections import deque
        answer = []
        queue = deque([[entrance[0], entrance[1], 0]])
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        seen = {(entrance[0],entrance[1])}

        while queue:

            for _ in range(len(queue)):
                height, width, step = queue.popleft()

                for x,y in dir:
                    next_height = height + x
                    next_width = width + y
                    
                    if next_height == -1 or next_height == h or next_width == -1 or next_width == w:
                        if step != 0:
                            return step
                        continue
                    if maze[next_height][next_width] == "+":
                        continue
                    if (next_height, next_width) not in seen:
                        queue.append([next_height, next_width, step + 1])
                        seen.add((next_height, next_width))
                        
        return -1