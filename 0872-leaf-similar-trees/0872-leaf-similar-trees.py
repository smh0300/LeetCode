# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    
        from collections import deque
        
        def dfs(tree):
            queue = deque()
            queue.append([tree,tree.val])
            
            answer = []
            
            while queue:
                cur_leaf, cur_val = queue.pop()
                
                if cur_leaf.left:
                    queue.append([cur_leaf.left, cur_leaf.left.val])
                    
                if cur_leaf.right:
                    queue.append([cur_leaf.right, cur_leaf.right.val])
            
                if cur_leaf.left == None and cur_leaf.right == None:
                    answer.append(cur_val)
            return answer
        
        a1 = dfs(root1)
        print(a1)
        
        a2 = dfs(root2)
        print(a2)
        
        return True if a1==a2 else False