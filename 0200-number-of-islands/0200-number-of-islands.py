class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x,y):
            visit[x][y] = 1

            #상
            if 0 <= x-1 and grid[x-1][y]!='0' and visit[x-1][y]==0:
                bfs(x-1,y)
            #하
            if x+1 <= len(grid)-1 and grid[x+1][y]!='0' and visit[x+1][y]==0:
                bfs(x+1,y)
            #좌
            if 0 <= y-1 and grid[x][y-1]!='0' and visit[x][y-1]==0:
                bfs(x,y-1)
            #우
            if y+1 <= len(grid[0])-1 and grid[x][y+1]!='0' and visit[x][y+1]==0:
                bfs(x,y+1)


        visit = [[0 for x in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]=='1' and visit[x][y]==0:
                    bfs(x,y)
                    count += 1
                else:
                    visit[x][y]=1
        return count