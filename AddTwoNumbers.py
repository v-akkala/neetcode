# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        carry = 0
        while l1 or l2:
            if not l1:
                s = l2.val 
            elif not l2:
                s = l1.val
            else:
                s = l1.val + l2.val
            cur.val = (s + carry) % 10
            if s + carry >= 10:
                carry = 1
            else:
                carry = 0
            prev = cur
            cur.next = ListNode()
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            cur.val = 1
        else:
            prev.next = None
        return head
