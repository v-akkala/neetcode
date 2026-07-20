# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        listheap = []
        counter = 0
        for ll in lists:
            cur = ll
            while cur != None:
                heapq.heappush(listheap, (cur.val, counter, cur))
                counter += 1
                cur = cur.next
        if len(listheap) == 0:
            return None
        dummy1, dummy2, start = heapq.heappop(listheap)
        cur = start
        while listheap:
            dummy1, dummy2, cur.next = heapq.heappop(listheap)
            cur = cur.next
        cur.next = None
        return start
