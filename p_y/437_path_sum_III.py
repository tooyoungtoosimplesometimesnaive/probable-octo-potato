# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def find_path(root, sum, current_sum):
            if root == None:
                return

            if root.val + current_sum == sum:
                self.result += 1
            find_path(root.left, sum, current_sum + root.val)
            find_path(root.right, sum, current_sum + root.val)

        def dfs(root, sum):
            if root == None:
                return
            
            find_path(root, sum, 0)
            dfs(root.left, sum)
            dfs(root.right, sum)
            
        dfs(root, sum)
        return self.result

# Better solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0
        self.cache = {0: 1}
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def find_path(root, sum, current_sum):
            if root == None:
                return

            current_sum += root.val
            old_sum = current_sum - sum
            self.result += self.cache.get(old_sum, 0)

            self.cache[current_sum] = self.cache.get(current_sum, 0) + 1
            find_path(root.left, sum, current_sum)
            find_path(root.right, sum, current_sum)
            self.cache[current_sum] -= 1

        find_path(root, sum, 0)
        return self.result

