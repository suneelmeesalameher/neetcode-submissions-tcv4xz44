# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result=[]
        queue=deque([root])
        while queue:
            current_level=[]
            queue_length=len(queue)
            for _ in range(queue_length):
                current_node= queue.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_level)
        return len(result)
        