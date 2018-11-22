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

