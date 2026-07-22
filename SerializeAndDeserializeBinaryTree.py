# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None "
        return str(root.val) + " " + self.serialize(root.left) + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.tree = deque(data.split(" "))
        self.tree.pop()
        if self.tree[0] == "None":
            return None
        cur = TreeNode(int(self.tree.popleft()))
        cur.left = self.build(self.tree.popleft())
        cur.right = self.build(self.tree.popleft())
        return cur
    
    def build(self, val):
        if val == "None":
            return None
        if len(self.tree) == 0:
            return
        cur = TreeNode(int(val))
        cur.left = self.build(self.tree.popleft())
        cur.right = self.build(self.tree.popleft())
        return cur

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
