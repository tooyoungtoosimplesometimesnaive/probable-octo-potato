# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def get_sum(root, sum, result, current_sum, current_path):
            if root == None:
                return
            if root.left == None and root.right == None:
                if root.val + current_sum == sum:
                    current_path.append(root.val)
                    result.append(current_path.copy())
                    current_path.pop()
                    return
                else:
                    return
            current_path.append(root.val)
            get_sum(root.left, sum, result, current_sum + root.val, current_path)
            get_sum(root.right, sum, result, current_sum + root.val, current_path)
            current_path.pop()

        result = []
        get_sum(root, sum, result, 0, [])
        return result

