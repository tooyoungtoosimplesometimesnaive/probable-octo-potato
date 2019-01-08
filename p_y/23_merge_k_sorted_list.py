# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pool = []
        
        # initialize:
        for list_node in lists:
            if list_node:
                heapq.heappush(pool, (list_node.val, list_node))
        result = ListNode(-1)
        p = result
        while pool:
            next_val, next_node = heapq.heappop(pool)
            
            p.next = next_node
            p = p.next
            if next_node.next:
                heapq.heappush(pool, (next_node.next.val, next_node.next))
        
        return result.next


# Take two:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []

        pq_pool = []
        for l in lists:
            if l != None:
                heapq.heappush(pq_pool, (l.val, l))

        dummy_head = ListNode(0)
        p = dummy_head
        while len(pq_pool) > 0:
            next_node_val, next_node = heapq.heappop(pq_pool)
            p.next = next_node
            p = p.next

