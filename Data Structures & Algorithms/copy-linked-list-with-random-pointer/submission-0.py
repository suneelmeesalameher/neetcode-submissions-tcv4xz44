"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mydir={None:None}
        curr=head
        
        while curr:
            newnode = Node(curr.val)
            mydir[curr]=newnode
            curr=curr.next
        
        curr=head
        while curr:
            copy=mydir[curr]
            copy.next=mydir[curr.next]
            copy.random=mydir[curr.random]
            curr=curr.next

        return mydir[head]

        
