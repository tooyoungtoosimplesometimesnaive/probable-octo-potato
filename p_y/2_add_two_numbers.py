# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        p1 = l1
        p2 = l2
        result = ListNode(-1)
        p = result
        while p1 != None and p2 != None:
            s = (p1.val + p2.val + carry) % 10
            carry = (p1.val + p2.val + carry) // 10
            p.next = ListNode(s)
            p1 = p1.next
            p2 = p2.next
            p = p.next
        
        p_remain = p1 if p1 != None else p2
        
        while p_remain != None:
            s = (p_remain.val + carry) % 10
            carry = (p_remain.val + carry) // 10
            p.next = ListNode(s)
            p = p.next
            p_remain = p_remain.next
        
        if carry != 0:
            p.next = ListNode(carry)

        return result.next

