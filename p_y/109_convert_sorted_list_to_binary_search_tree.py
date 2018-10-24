# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helper(head, last):
            if head == None:
                return None
            if head == last:
                return None
            p_fast = head
            p_slow = head
            while p_fast != last and p_fast.next != last:
                p_fast = p_fast.next.next
                p_slow = p_slow.next
            
            root = TreeNode(p_slow.val)
            left = helper(head, p_slow)
            right = helper(p_slow.next, last)
            root.left = left
            root.right = right
            return root
            
        return helper(head, None)

# After referencing others' solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.list = None
    def sortedListToBST(self, head):
        # This is O(2n) O(n)
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def count(head):
            p = head
            c = 0
            while p != None:
                p = p.next
                c += 1
            return c
        def generate(n):
            if n == 0:
                return None
            root = TreeNode(0)
            root.left = generate( n // 2 )
            root.val = self.list.val
            self.list = self.list.next
            root.right = generate(n - (n // 2) - 1)
            return root

        self.list = head
        n = count(head)

        return generate(n)

