# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        ans=[]
        if not root:
            return result
        queue=deque([root])
        while queue:
            queue_length=len(queue)
            current_level=[]
            for _ in range(queue_length):
                current_node=queue.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_level)

        for x in result:
            ans.append(x[-1])
        return ans    