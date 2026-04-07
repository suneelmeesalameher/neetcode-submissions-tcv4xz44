# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=[]
        queue=deque([root])
        while queue:
            queueLength=len(queue)
            #currentLevel=[]
            for _ in range(queueLength):
                currentNode=queue.popleft()
                result.append(currentNode.val)
                if(currentNode.left):
                    queue.append(currentNode.left)
                if(currentNode.right):
                    queue.append(currentNode.right)
            #result.append(currentLevel)
        heapq.heapify(result)
        for i in range(k):
            ans=heapq.heappop(result)
        return ans