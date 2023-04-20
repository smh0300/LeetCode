class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(x,y):
            global count # global변수도 함수내의 지역변수로 사용하게 설정(2/2)
            visit[x][y] = 1
            count += 1
            #상
            if 0 <= x-1 and grid[x-1][y]!=0 and visit[x-1][y]==0:
                bfs(x-1,y)
            #하
            if x+1 <= len(grid)-1 and grid[x+1][y]!=0 and visit[x+1][y]==0:
                bfs(x+1,y)
            #좌
            if 0 <= y-1 and grid[x][y-1]!=0 and visit[x][y-1]==0:
                bfs(x,y-1)
            #우
            if y+1 <= len(grid[0])-1 and grid[x][y+1]!=0 and visit[x][y+1]==0:
                bfs(x,y+1)

        counts=[0]
        visit = [[0 for x in range(len(grid[0]))] for _ in range(len(grid))]
        global count # global변수도 함수내의 지역변수로 사용하게 설정(1/2)
        count = 0


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1 and visit[x][y]==0:
                    bfs(x,y)
                    counts.append(count)
                    count = 0
                else:
                    visit[x][y]=1
        return max(counts)