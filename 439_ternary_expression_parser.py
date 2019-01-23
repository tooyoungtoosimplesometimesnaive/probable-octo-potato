class TreeNode:
    def __init__(self, v, left, right):
        self.value = v
        self.left = left
        self.right = right
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        root = self.construct_tree(list(expression))

        while root != None:
            if root.left == None and root.right == None:
                break
            if root.value == 'T':
                root = root.left
            elif root.value == 'F':
                root = root.right

        return root.value

    def construct_tree(self, expression):
        if len(expression) == 0:
            return None

        value = expression.pop(0)

        if len(expression) == 0:
            return TreeNode(value, None, None)
        next_char = expression.pop(0)
        if next_char == '?':
            left = self.construct_tree(expression)
            right = self.construct_tree(expression)
            return TreeNode(value, left, right)
        else:
            return TreeNode(value, None, None)

# take 2:
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def __init__(self):
        self.p = 0

    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        t = self.tree(expression)
        #print(t.val, t.left.val, t.right.val)
        return self.walk(t)

    def tree(self, expression):
        if expression == None or len(expression) == 0 or self.p >= len(expression):
            return None
        root = TreeNode(expression[self.p])
        self.p += 1

        if self.p < len(expression) and expression[self.p] == ':':
            self.p += 1
            return root
        self.p += 1
        root.left = self.tree(expression)
        root.right = self.tree(expression)

        return root

    def walk(self, t):
        if t.left == None and t.right == None:
            return t.val
        elif t.val == 'F':
            return self.walk(t.right)
        else:
            return self.walk(t.left)

