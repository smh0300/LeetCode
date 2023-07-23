class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        h,w = len(grid), len(grid[0])
        queue = deque([])
        visit = set()
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        height, width, minute = 0, 0, 0
        for y,x in enumerate(grid):
            for a,b in enumerate(x):
                if b==2:
                    width = a
                    height = y
                    queue.append([height, width, minute])

        while queue:
            height, width, minute = queue.popleft()
            for x,y in dir:
                next_height = height + x
                next_width = width + y
                if 0 <= next_height < h and 0 <= next_width < w:
                    if grid[next_height][next_width] == 0 or grid[next_height][next_width] == 2:
                        continue
                    if grid[height][width] == 2:
                        grid[next_height][next_width] = 2
                        queue.append([next_height, next_width, minute + 1])

        for x in grid:
            if 1 in x:
                return -1
        return minute