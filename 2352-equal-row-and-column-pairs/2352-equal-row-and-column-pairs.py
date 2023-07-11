class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_reverse = []
        for x in range(len(grid)):
            a = []
            for y in range(len(grid[0])):
                a.append(grid[y][x])
            grid_reverse.append(a)

        answer = 0
        for x in grid:
            if x in grid_reverse:
                answer += grid_reverse.count(x)
        return answer