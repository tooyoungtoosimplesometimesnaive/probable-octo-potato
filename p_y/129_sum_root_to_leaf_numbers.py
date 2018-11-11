# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_all(root, result, current_path):
            if root == None:
                return
            
            if root.left == None and root.right == None:
                result.append(current_path + [root.val])
                return
            get_all(root.left, result, current_path + [root.val])
            get_all(root.right, result, current_path + [root.val])
        
        def to_num(list):
            if len(list) == 0:
                return 0
            return list[-1] + 10 * to_num(list[:-1])
        
        # print(to_num([4,0,9,6]))
            
        result = []
        get_all(root, result, [])
        
        return sum(map(lambda p: to_num(p), result))


