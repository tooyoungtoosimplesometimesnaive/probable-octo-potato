class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers_map = collections.defaultdict(int)
        self.list = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.numbers_map[number] += 1
        self.list.append(number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.list:
            if n == value - n:
                if n == value - n and self.numbers_map[n] >= 2:
                    return True
            elif value - n in self.numbers_map:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
