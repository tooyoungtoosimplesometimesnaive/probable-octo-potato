class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.update_traverse(root, 0)
        return root
    
    def update_traverse(self, root, parent_sum):
        if root == None:
            return
        root_right_sum = self.sum_traverse(root.right)
        original = root.val
        root.val += parent_sum + root_right_sum

        self.update_traverse(root.left, root.val)
        self.update_traverse(root.right, root.val - original - root_right_sum)
        
    def sum_traverse(self, root):
        if root == None:
            return 0
        left_sum = self.sum_traverse(root.left)
        right_sum = self.sum_traverse(root.right)

        return left_sum + root.val + right_sum


class Solution:
    s = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        self.convertBST(root.right)
        original = root.val
        root.val += self.s
        self.s += original
        self.convertBST(root.left)
        return root
