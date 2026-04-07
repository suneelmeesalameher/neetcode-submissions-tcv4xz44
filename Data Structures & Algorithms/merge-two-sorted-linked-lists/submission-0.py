# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        newList=ListNode(0)
        current=newList
        while head1 and head2:
            #if head1 and head2:
            if head1.val<head2.val:
                newListNode=ListNode(head1.val)
                current.next=newListNode
                current=current.next
                head1=head1.next
                
            else:
                newListNode=ListNode(head2.val)
                current.next=newListNode
                current=current.next
                head2=head2.next
        if head1 is not None:
            current.next=head1
        if head2 is not None:
            current.next=head2
        return newList.next
