# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, sums):
            nonlocal count
            
            if root is None:
                return
            
            sums += root.val
            if sums == targetSum:
                count += 1
            
            dfs(root.left, sums)
            dfs(root.right, sums)
        
        def iteratorDfs(root):
            if root is None:
                return
            dfs(root,0)
            iteratorDfs(root.left)
            iteratorDfs(root.right)
            
        count = 0
        iteratorDfs(root)
        
        return count