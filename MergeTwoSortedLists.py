# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp
        l1prev = None
        cur = list1
        l1next = list1.next
        start = list1
        while list2 and l1next:
            if l1next.val < list2.val:
                    l1prev = cur
                    cur = l1next
                    l1next = l1next.next
                    continue
            if cur.val <= list2.val:
                l1prev = cur
                l2next = list2.next
                cur.next = list2
                list2.next = l1next
                cur = list2
                list2 = l2next
                continue
        if not l1next:
            cur.next = list2
        return start
