# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        def bfs(root,depth):
            queue = deque()
            queue.append([root,depth])
            answer = {}
            while queue:
                cur_node, depth = queue.popleft()
                if depth in answer:
                    answer[depth] += cur_node.val
                else:
                    answer[depth] = cur_node.val
                
                depth += 1
                if cur_node.left:
                    queue.append([cur_node.left,depth])
                if cur_node.right:
                    queue.append([cur_node.right,depth])
                
            return answer
        
        answer = bfs(root, 1)
        maxval = max(answer.values())
        return [k for k,v in answer.items() if v == maxval][0]
        