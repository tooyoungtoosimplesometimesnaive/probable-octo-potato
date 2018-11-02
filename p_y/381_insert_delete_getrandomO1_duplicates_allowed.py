class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {} # int -> set(int)
        self.list = []
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            self.map[val].add(self.size)
            self.size += 1
            self.list.append(val)
            return False
        else:
            self.map[val] = {self.size}
            self.size += 1
            self.list.append(val)

            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        original_id = self.map[val].pop() # get one 
        
        # if there is no more element of val in the map, remove the entry
        if len(self.map[val]) == 0:
            self.map.pop(val)

        if original_id == len(self.list) - 1:
            self.list.pop()
            self.size -= 1
        else:
            last = self.list.pop()
            self.list[original_id] = last
            self.map[last].remove(len(self.list))
            self.map[last].add(original_id)
            self.size -= 1
            
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.list[random.randrange(0, self.size)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
