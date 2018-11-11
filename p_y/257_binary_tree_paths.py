# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def get_all_paths(root, result, current_path):
            if root == None:
                return
            
            # Add only when there we reach leaf node:
            if root.left == None and root.right == None:
                result.append(current_path + [root.val])
                return
            
            get_all_paths(root.left, result, current_path + [root.val])
            get_all_paths(root.right, result, current_path + [root.val])
            
        result = []
        get_all_paths(root, result, [])
        print(result)
        
        return list(map(lambda path : "->".join([str(n) for n in path]), result))

