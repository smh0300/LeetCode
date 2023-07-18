# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxx):
            nonlocal count
            if root is None:
                return
            else:
                if root.val >= maxx:
                    count += 1
                    maxx = max(maxx, root.val)
            dfs(root.left, maxx)
            dfs(root.right, maxx)
        
        count = 0
        dfs(root, root.val)
        
        
        return count