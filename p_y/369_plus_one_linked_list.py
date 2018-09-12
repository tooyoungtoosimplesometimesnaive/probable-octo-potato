# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        def rev(n):
            if n.next == None:
                return n
            new_head = rev(n.next)
            n.next.next = n
            n.next = None
            return new_head

        r = rev(head)
        p = r
        pp = None
        carry = 1
        while p != None:
            new_val = (p.val + carry) % 10
            carry = (p.val + carry) // 10
            p.val = new_val
            pp = p
            p = p.next
            
        if carry == 1:
            pp.next = ListNode(1)
            
        return rev(r)
