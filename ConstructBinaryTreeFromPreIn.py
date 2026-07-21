# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.treehash = {}
        for i, v in enumerate(inorder):
            self.treehash[v] = i
        self.preidx = 0
        val = preorder[self.preidx]
        left = self.build(preorder, inorder, 0, self.treehash[val] - 1)
        right = self.build(preorder, inorder, self.treehash[val] + 1, len(inorder) - 1)
        return TreeNode(val, left, right)
    
    def build(self, preorder, inorder, leftorder, rightorder):
        if leftorder > rightorder:
            return None
        self.preidx += 1
        if self.preidx >= len(preorder):
            return None
        val = preorder[self.preidx]
        idx = self.treehash[val]
        left = self.build(preorder, inorder, leftorder, idx - 1)
        right = self.build(preorder, inorder, idx + 1, rightorder)
        return TreeNode(val, left, right)

