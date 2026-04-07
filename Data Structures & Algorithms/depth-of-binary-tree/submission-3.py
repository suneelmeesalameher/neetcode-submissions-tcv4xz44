# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth=0
        if not root:
            maxdepth=0
            return maxdepth
        #if root.left and root.right:
        maxdepth=max(self.maxDepth(root.left) if root.left else 0,self.maxDepth(root.right)if root.right else 0)+1
        
        return maxdepth
        