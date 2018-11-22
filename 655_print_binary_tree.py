class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if root == None:
            return [[]]
        
        row = self.height(root)
        col = 2**row - 1
        
        matrix = [["" for _ in range(col)] for _ in range(row)]
        
        self.fill_in(root, 0, 0, col, matrix)
        return matrix
    
    def fill_in(self, root, level, left, right, matrix):
        if root == None:
            return
        mid = (left + right) // 2
        matrix[level][mid] = str(root.val)
        self.fill_in(root.left, level + 1, left, mid - 1, matrix)
        self.fill_in(root.right, level + 1, mid + 1, right, matrix)
    
    def height(self, root):
        if root == None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

