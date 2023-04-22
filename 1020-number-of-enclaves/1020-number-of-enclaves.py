class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()


        def dfs(r,c):
            if (r < 0 or c <0 or r==ROWS or c==COLS):
                return 0
            if grid[r][c] == 0 or (r,c) in visit:
                return 1

            visit.add((r,c))
            global count 
            count += 1
            return min(dfs(r+1,c),
                       dfs(r-1,c),
                       dfs(r,c+1),
                       dfs(r,c-1))


        global count
        count = 0
        counts = 0
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0 and (r,c) not in visit:
                    res = dfs(r,c)
                    if res == 1:
                        counts += count
                    count = 0
                    
        return counts