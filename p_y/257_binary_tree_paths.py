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

# Take 2:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        self.get_paths(result, [], root)
        #print(result)
        result = list(map(lambda l: "->".join(l), result))

        return result

    def get_paths(self, result, current, node):
        if node == None:
            return

        if node.left == None and node.right == None:
            current.append(str(node.val))
            result.append(current.copy())
            current.pop(-1)
            return

        current.append(str(node.val))
        self.get_paths(result, current, node.left)
        self.get_paths(result, current, node.right)
        current.pop(-1)

