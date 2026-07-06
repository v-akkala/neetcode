# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        start = root
        nodes = deque([root])
        while nodes:
            cur = nodes.popleft()
            if cur:
                temp = cur.right
                cur.right = cur.left
                cur.left = temp
                nodes.append(cur.left)
                nodes.append(cur.right)
        return start
