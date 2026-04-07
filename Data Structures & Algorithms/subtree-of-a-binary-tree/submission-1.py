# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sametree(Node1: TreeNode, Node2: TreeNode)-> bool:
            if Node1 is None and Node2 is None:
                return True
            if Node1 is None or Node2 is None:
                return False
            if Node1.val != Node2.val:
                return False
            return sametree(Node1.left, Node2.left) and sametree(Node1.right, Node2.right)
        
        if not root:
            return False
        
        if not subRoot:
            return True

        if sametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
