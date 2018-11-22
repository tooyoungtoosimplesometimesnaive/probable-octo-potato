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
        if root == None:
            return '#'
        else:
            return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == None or len(data) == 0:
            return None
        data = data.split(',')
        root = self.d(data)
        return root

    def d(self, data):
        if data[0] == '#':
            data.pop(0)
            return None

        root = TreeNode(int(data[0]))
        data.pop(0)
        root.left = self.d(data)
        root.right = self.d(data)
        return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
