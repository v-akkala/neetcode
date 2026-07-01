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
        if(list1.val < list2.val):
            start = list1
        else:
            start = list2
        l1prev = list1
        l2prev = list2
        while list1 and list2:
            if list1.next:
                if list1.next.val <= list2.val:
                    list1 = list1.next
                    continue
            elif list2.next:
                if list2.next.val <= list1.val:
                    list2 = list2.next
                    continue
            if list1.val <= list2.val:
                l1next = list1.next
                list1.next = list2
                list1 = l1next
                continue
            if list1.val > list2.val:
                l2next = list2.next
                list2.next = list1
                list2 = l2next
                continue
        if not (list1 or list2):
            return start
        if not list1:
            list1.next = list2
        if not list2:
            list2.next = list1
        return start
