# Definition for a binary tree node.
class node:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

from collections import deque

def bfs(a):

  if a==None:
    return 0

  b=deque()
  b.append([a,1])
  max_depth=0

  while b:
    cur_node, cur_depth = b.popleft()
    max_depth = max(max_depth, cur_depth)
    cur_depth += 1
    if cur_node.left:
        b.append([cur_node.left, cur_depth])
    
    if cur_node.right:
        b.append([cur_node.right, cur_depth])

  return max_depth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return bfs(root)

