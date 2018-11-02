class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.size = 0
        self.list = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        #print("insert: {} {}".format(val, self.map))
        if val in self.map:
            return False
        self.list.append(val)
        self.map[val] = self.size
        self.size += 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        #print("remove: {} {}".format(val, self.map))

        if val not in self.map:
            return False
        original_id = self.map[val]
        self.map.pop(val)

        last_one = self.list[-1]
        self.list[original_id] = last_one
        
        if original_id != len(self.list) - 1: # if the removed element is not the last one
            self.map[last_one] = original_id
        self.list.pop(-1)
        self.size -= 1

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.list[random.randrange(0, self.size)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
