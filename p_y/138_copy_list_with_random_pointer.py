# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None

        original_head = head
        copied_dict = {}

        while head != None:
            p = None
            if head not in copied_dict:
                p = RandomListNode(head.label)
                copied_dict[head] = p
            else:
                p = copied_dict[head]

            if head.random != None:
                if head.random not in copied_dict:
                    r = RandomListNode(head.random.label)
                    p.random = r
                    copied_dict[head.random] = r
                else:
                    p.random = copied_dict[head.random]

            if head.next != None:
                if head.next not in copied_dict:
                    n = RandomListNode(head.next.label)
                    p.next = n
                    copied_dict[head.next] = n
                else:
                    p.next = copied_dict[head.next]
                
            head = head.next

        return copied_dict[original_head]


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None

        original_head = head
        copied_dict = {}

        while head != None:
            node = RandomListNode(head.label)
            copied_dict[head] = node
            head = head.next

        head = original_head
        while head != None:
            n = copied_dict[head.next] if head.next != None else None
            r = copied_dict[head.random] if head.random != None else None
            this = copied_dict[head]
            this.next = n
            this.random = r
            head = head.next

        return copied_dict[original_head]

