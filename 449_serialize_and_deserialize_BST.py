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
            return ""
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        result = str(root.val)
        result += "" if left == "" else "," + left
        result += "" if right == "" else "," + right
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        data = list(map(lambda x: int(x), data.split(",")))
        return self.d(data)

    def d(self, data):
        if len(data) == 0:
            return None
        root_val = data.pop(0)
        root = TreeNode(root_val)
        
        left_data = list(filter(lambda x: x < root_val, data))
        right_data = list(filter(lambda x: x > root_val, data))

        root.left = self.d(left_data)
        root.right = self.d(right_data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Another solution:
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
            return ""
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        result = str(root.val)
        result += "" if left == "" else "," + left
        result += "" if right == "" else "," + right
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        data = list(map(lambda x: int(x), data.split(",")))
        return self.d(data, float('inf'))

    def d(self, data, parent):
        if len(data) == 0:
            return None

        if data[0] > parent:
            return None

        root = TreeNode(data[0])
        data.pop(0)
        root.left = self.d(data, root.val)
        root.right = self.d(data, parent)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

