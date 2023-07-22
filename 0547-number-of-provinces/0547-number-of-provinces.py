class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import deque
        ls = deque([] for _ in range(len(isConnected)))
        
        for x in range(len(isConnected)):
            for y in range(len(isConnected[0])):
                if isConnected[x][y] == 1:
                    ls[x].append(y)
        print(ls)
             
        count = 0
        visit = [0 for _ in range(len(isConnected))]     
        while 0 in visit:
                        
            next_explore = visit.index(0)
            nodes = [x for x in ls[next_explore]]
            visit[next_explore] = 1
            
            while nodes:
                next_node = nodes.pop()
                if visit[next_node] == 0:
                    visit[next_node]=1
                    for x in ls[next_node]:
                        nodes.append(x)

            count += 1
            
        return count