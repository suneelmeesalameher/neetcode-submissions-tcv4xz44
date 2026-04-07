# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0,None)
        head=l3
        carry=0
        
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            overallsum = val1+val2+carry
            carry=overallsum//10
            newNode=ListNode(overallsum%10)
            l3.next=newNode
            l3=l3.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return head.next
        
        # reversel1=l1
        # reversel2=l2
        # carry=0
        # while reversel1 and reversel2:
        #     #if reversel1 and reversel2:
        #     overallsum=reversel1.val+reversel2.val+carry
        #     if overallsum<10:   
        #         newNode=ListNode(overallsum)
        #         l3.next=newNode
        #         l3=l3.next
        #         carry=0
        #     else:
        #         carry=1
        #         newNode=ListNode(overallsum%10)
        #         l3.next=newNode
        #         l3=l3.next
        #     reversel1=reversel1.next
        #     reversel2=reversel2.next

        # while reversel1 and not reversel2:
        #     overallsum=reversel1.val+carry
        #     if overallsum<10:
        #         newNode=ListNode(overallsum%10,reversel1.next)
        #         carry=0
        #         l3.next=newNode
        #         l3=l3.next
        #         break
        #     else:
        #         newNode=ListNode(overallsum%10)
        #         carry=1
        #         l3.next=newNode
        #         l3=l3.next
        #         reversel1=reversel1.next


        # while reversel2 and not reversel1:
        #     overallsum=reversel2.val+carry
        #     if overallsum<10:
        #         newNode=ListNode(overallsum%10,reversel2.next)
        #         carry=0
        #         l3.next=newNode
        #         l3=l3.next
        #         break
        #     else:
        #         newNode=ListNode(overallsum%10)
        #         carry=1
        #         l3.next=newNode
        #         l3=l3.next
        #         reversel2=reversel2.next

        # if not reversel1 and not reversel2 and carry:
        #     newNode=ListNode(carry)
        #     l3.next=newNode
        #     l3=l3.next
        #     carry=0
        # return head.next
