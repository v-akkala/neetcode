# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        end = head
        prev = head
        next = head.next
        counter = 0
        while end:
            counter += 1
            end = end.next
        stravel = counter - n
        for x in range(0, stravel):
            prev = cur
            cur = cur.next
            next = cur.next
        if stravel == 0:
            return head.next
        prev.next = next
        return head


