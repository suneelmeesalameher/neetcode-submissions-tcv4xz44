# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        mainans=[]
        if not root:
            return ans
        queue= deque([root])
        while queue:
            length=len(queue)
            sublist=[]
            while length:
                node=queue.popleft()
                value=node.val
                sublist.append(value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                length-=1
            ans.append(sublist)
        for l in ans:
            mainans.append(l[-1])

        return mainans