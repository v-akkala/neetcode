# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            higher = p
            lower = q
        else: 
            higher = q
            lower = p
        while not (root.val <= higher.val and root.val >= lower.val):
            if root.val > higher.val and root.val > lower.val:
                root = root.left
            elif root.val < higher.val and root.val < lower.val:
                root = root.right
        return root

