class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = Node(-1)
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        #print('get')
        if index >= self.size:
            return -1
        p = self.moveToPosition(index)
        return p.next.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        #print('add at head, size={}'.format(self.size))
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        #print('add at tail, size={}'.format(self.size))
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        #print('add at index={}, size={}, val={}'.format(index, self.size, val))
        # if self.head.next != None:
        #     print('head={}'.format(self.head.next.val))

        if index > self.size:
            return
            
        p = self.moveToPosition(index)
        newNode = Node(val)
        newNode.next = p.next
        p.next = newNode
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        #print('delete at index {}'.format(index))
        if index >= self.size:
            return
        p = self.moveToPosition(index)

        p.next = p.next.next
        self.size -= 1

    def moveToPosition(self, index):
        p = self.head
        i = 0
        while i < index:
            p = p.next
            i += 1
        return p
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
