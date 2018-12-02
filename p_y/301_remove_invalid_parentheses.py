# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0

    def get_height(self, root):
        if root == None:
            return 0
        return self.get_height(root.left) + 1

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        h_left = self.get_height(root.left)
        h_right = self.get_height(root.right)
        if h_left != h_right:
            return self.countNodes(root.left) + 1 + 2 ** h_right - 1
        else:
            return self.countNodes(root.right) + 1 + 2 ** h_left - 1
        
# Another way:
#
class Solution:
    def is_valid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count > 0:
                    count -= 1
                else:
                    return False
        return count == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #print(self.is_valid(s))
        result = set()
        visited = set()
        q = list()
        found = False
        
        q.append(s)
        while q:
            top = q.pop(0)
            # print(top)
            if (self.is_valid(top)):
                found = True
                result.add(top)
            if found:
                continue
            
            for i in range(len(top)):
                if top[i] == '(' or top[i] == ')':
                    next_str = top[:i] + top[i + 1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        q.append(next_str)
        
        return list(result)

# Take 2:
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left_unmatch, right_unmatch = self.calc_unmatched_parentheses(s)
        # print(left_unmatch, right_unmatch)
        result = set()
        self.dfs(s, 0, "", result, left_unmatch, right_unmatch)
        return list(result)

    def calc_unmatched_parentheses(self, s):
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return (left, right)

    def is_valid(self, s):
        left, right = self.calc_unmatched_parentheses(s)
        return left == 0 and right == 0

    def dfs(self, s, i, current, result, left_unmatch, right_unmatch):
        #print(current, i)
        if i == len(s):
            if left_unmatch == 0 and right_unmatch == 0 and self.is_valid(current):
                # print("hhhhh")
                # print(s)
                result.add(current)
            return

        if s[i] != '(' and s[i] != ')':
            self.dfs(s, i + 1, current + s[i], result, left_unmatch, right_unmatch)
        else:
            self.dfs(s, i + 1, current + s[i], result, left_unmatch, right_unmatch)
            if s[i] == '(' and left_unmatch > 0:
                self.dfs(s, i + 1, current, result, left_unmatch - 1, right_unmatch)
            elif s[i] == ')' and right_unmatch > 0:
                self.dfs(s, i + 1, current, result, left_unmatch, right_unmatch - 1)

