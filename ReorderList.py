
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        stack = deque()
        cur = head
        while temp:
            stack.append(temp)
            temp = temp.next
        parity = len(stack) % 2 == 0
        if parity:
            c = len(stack) // 2 - 1
        else:
            c = len(stack) // 2
        for x in range(0, c):
            next = cur.next
            cur.next = stack.pop()
            cur = cur.next
            cur.next = next
            cur = next
        if parity:
            cur.next.next = None
        else:
            cur.next = None
