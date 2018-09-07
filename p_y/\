# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def list_len(node):
            return 0 if node == None else 1 + list_len(node.next)
        def add_front(v, node):
            new_node = ListNode(v)
            new_node.next = node
            return new_node

        curr1 = l1
        curr2 = l2
        n1 = list_len(l1)
        n2 = list_len(l2)
        result = None
        while n1 > 0 and n2 > 0:
            s = 0
            if n1 >= n2:
                s += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n2 > n1:
                s += curr2.val
                curr2 = curr2.next
                n2 -= 1
            result = add_front(s, result)

        carry = 0
        curr = result
        result = None
        while curr != None:
            curr.val += carry
            carry = curr.val // 10
            result = add_front(curr.val % 10, result)
            curr = curr.next
                
        if carry > 0:
            result = add_front(1, result)
        return result
        
