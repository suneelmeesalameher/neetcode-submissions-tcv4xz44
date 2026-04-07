# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0,None)
        head=l3
        reversel1=l1
        reversel2=l2
        carry=0
        while reversel1 and reversel2:
            #if reversel1 and reversel2:
            overallsum=reversel1.val+reversel2.val+carry
            if overallsum<10:   
                newNode=ListNode(overallsum)
                l3.next=newNode
                l3=l3.next
                carry=0
            else:
                carry=1
                newNode=ListNode(overallsum%10)
                l3.next=newNode
                l3=l3.next
            reversel1=reversel1.next
            reversel2=reversel2.next

        while reversel1 and not reversel2:
            overallsum=reversel1.val+carry
            if overallsum<10:
                newNode=ListNode(overallsum%10,reversel1.next)
                carry=0
                l3.next=newNode
                l3=l3.next
                break
            else:
                newNode=ListNode(overallsum%10)
                carry=1
                l3.next=newNode
                l3=l3.next
                reversel1=reversel1.next


        while reversel2 and not reversel1:
            overallsum=reversel2.val+carry
            if overallsum<10:
                newNode=ListNode(overallsum%10,reversel2.next)
                carry=0
                l3.next=newNode
                l3=l3.next
                break
            else:
                newNode=ListNode(overallsum%10)
                carry=1
                l3.next=newNode
                l3=l3.next
                reversel2=reversel2.next

        if not reversel1 and not reversel2 and carry:
            newNode=ListNode(carry)
            l3.next=newNode
            l3=l3.next
            carry=0
        return head.next

    def reverse(self, l1:Optional[ListNode])->Optional[ListNode]:
        prev=None
        curr=l1
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        return prev