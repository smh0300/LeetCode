class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict, deque
        node_dict = defaultdict(set)
        connections = set(((u,v) for u,v in connections))
        for u,v in connections:
            node_dict[u].add(v)
            node_dict[v].add(u)

        visit = [0] * n
        nodes = deque([0])
        count = 0 
        while nodes:
            cur_node = nodes.popleft()
            visit[cur_node] = 1
            for x in node_dict[cur_node]:
                if visit[x] == 0:
                    if (cur_node, x) in connections:
                        count += 1 
                    nodes.append(x)
                    
        return count