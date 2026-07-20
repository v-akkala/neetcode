# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kheap = []
        treeq = deque([root])
        while treeq:
            node = treeq.popleft()
            if node.left:
                treeq.append(node.left)
            if node.right:
                treeq.append(node.right)
            if len(kheap) == k:
                if node.val < -kheap[0]:
                    heapq.heappop(kheap)
                    heapq.heappush(kheap, -node.val)
            elif len(kheap) < k:
                heapq.heappush(kheap, -node.val)
        return -kheap[0]
