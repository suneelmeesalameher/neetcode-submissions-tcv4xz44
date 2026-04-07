# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxdiameter=0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root:Optinal[TreeNode]):
            if not root:
                return 0

            #maxdepth=max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))+1
            self.maxdiameter=max((dfs(root.left)+dfs(root.right)), self.maxdiameter)
            return max(dfs(root.left),dfs(root.right))+1

        dfs(root)
        return self.maxdiameter
    
