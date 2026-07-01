# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        visited = set()
        traverser = head
        while traverser:
            visited.add(traverser)
            traverser = traverser.next
            if traverser in visited:
                return True
        return False
