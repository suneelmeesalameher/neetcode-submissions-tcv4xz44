# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(p,q, root):
            if root.val==p.val:
                return p
            if root.val==q.val:
                return q
            if p.val<root.val<q.val:
                return root
            elif root.val<p.val:
                return dfs(p,q,root.right)
            elif root.val>q.val:
                return dfs(p,q,root.left)
        if q.val<p.val:
            return dfs(q,p,root)
        else:
            return dfs(p,q,root)