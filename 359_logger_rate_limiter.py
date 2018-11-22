class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key: log message, value: time
        self.logs = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        
        if message not in self.logs:
            self.logs[message] = timestamp
            return True
        else:
            t = self.logs[message]
            if timestamp - t >= 10:
                self.logs[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

