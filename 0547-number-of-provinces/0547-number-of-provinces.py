class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(cur_node):
            visit[cur_node] = 1
            for idx,node in enumerate(isConnected[cur_node]):
                if node==1 and visit[idx]==0:
                    dfs(idx)




        visit = [0 for _ in range(len(isConnected))]
        count = 0
        for x in range(len(isConnected)):

            if visit[x] == 0:
                dfs(x)
                count += 1
        return count