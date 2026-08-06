# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def recurse(node):
            if not node:
                return 0
            if not (node.right or node.left):
                return 1
            left = recurse(node.left)
            right = recurse(node.right)
            self.d = max(self.d, left + right)
            return 1 + max(left, right)

        recurse(root)
        return self.d
