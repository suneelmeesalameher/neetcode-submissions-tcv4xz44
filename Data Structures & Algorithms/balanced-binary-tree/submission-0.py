# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(node):
            if node is None:
                return 0
            left_height= dfs(node.left)
            if left_height is False:
                return False
            right_height=dfs(node.right)
            if right_height is False:
                return False
            if abs(left_height-right_height)>1:
                return False
            return 1+max(left_height, right_height)
        if dfs(root):
            return True
        else:
            return False