class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]
        visit = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        def dfs(sr,sc):
            visit[sr][sc]=1
            if image[sr][sc] == initial_color:
                image[sr][sc] = color

                if sr-1 >= 0 and visit[sr-1][sc]==0: # 상
                    dfs(sr-1,sc)
                if sr+1 <= len(image)-1 and visit[sr+1][sc]==0: # 하
                    dfs(sr+1,sc)
                if sc-1 >= 0 and visit[sr][sc-1]==0: # 좌
                    dfs(sr,sc-1)
                if sc+1 <= len(image[0])-1 and visit[sr][sc+1]==0: # 우
                    dfs(sr,sc+1)
            else:
                return
            
        dfs(sr,sc)


        return image
        