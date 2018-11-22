"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root == None:
            return ""
        else:
            s = str(root.val) + "," + str(len(root.children))
            children_s = []
            for child in root.children:
                children_s.append(self.serialize(child))
            if len(children_s) > 0:
                return s + "," + ",".join(children_s)
            else:
                return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None
        data = data.split(',')
        return self.d(data)
    def d(self, data):
        if len(data) == 0:
            return None
        val = int(data.pop(0))
        children_num = int(data.pop(0))
        
        children = []
        for i in range(children_num):
            children.append(self.d(data))
        root = Node(val, children)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

