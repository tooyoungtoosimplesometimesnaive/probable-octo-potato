class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.delta[start] += 1
        self.delta[end] -= 1
        
        active = 0
        result = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > result:
                result = active
        return result


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

