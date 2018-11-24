# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        t = self.get_token(s)
        print(t)
        return self.parse(t)
    
    def parse(self, token):
        if token[0] != ']' and token[0] != '[':
            ni = NestedInteger(int(token.pop(0)))
            return ni

        ni = NestedInteger()
        token.pop(0)
        while token[0] != ']':
            ni.add(self.parse(token))
        token.pop(0)
        return ni

    def get_token(self, s):
        result = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                result.append('[')
                i += 1
            elif s[i] == ']':
                result.append(']')
                i += 1
            elif (s[i] <= '9' and s[i] >= '0') or s[i] == '-':
                is_negative = ''
                if s[i] == '-':
                    is_negative = '-'
                    i += 1
                num = ''
                while i < len(s) and s[i] <= '9' and s[i] >= '0':
                    num = num + s[i]
                    i += 1
                result.append(is_negative + num)
            else:
                i += 1
        
        return result

# Take 2
class Solution:
    def __init__(self):
        self.index = 0
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        t = self.get_token(s)
        # print(t)
        return self.parse(t)

    def parse(self, token):
        if token[self.index] != ']' and token[self.index] != '[':
            ni = NestedInteger(int(token[self.index]))
            self.index += 1
            return ni

        ni = NestedInteger()
        self.index += 1
        while self.index < len(token) and token[self.index] != ']':
            ni.add(self.parse(token))
        self.index += 1
        return ni

    def get_token(self, s):
        result = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                result.append('[')
                i += 1
            elif s[i] == ']':
                result.append(']')
                i += 1
            elif (s[i] <= '9' and s[i] >= '0') or s[i] == '-':
                is_negative = ''
                if s[i] == '-':
                    is_negative = '-'
                    i += 1
                num = ''
                while i < len(s) and s[i] <= '9' and s[i] >= '0':
                    num = num + s[i]
                    i += 1
                result.append(is_negative + num)
            else:
                i += 1

        return result

# Another way:
class Solution:
    def __init__(self):
        self.index = 0
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        t = self.get_token(s)
        print(t)
        return self.parse(t)

    def parse(self, token):
        if self.index > len(token):
            return None
        ni = NestedInteger()
        if token[self.index] == '[':
            self.index += 1
            while token[self.index] != ']':
                ni.add(self.parse(token))
            self.index += 1
        else:
            ni.setInteger(int(token[self.index]))
            self.index += 1
        return ni

    def get_token(self, s):
        result = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                result.append('[')
                i += 1
            elif s[i] == ']':
                result.append(']')
                i += 1
            elif (s[i] <= '9' and s[i] >= '0') or s[i] == '-':
                is_negative = ''
                if s[i] == '-':
                    is_negative = '-'
                    i += 1
                num = ''
                while i < len(s) and s[i] <= '9' and s[i] >= '0':
                    num = num + s[i]
                    i += 1
                result.append(is_negative + num)
            else:
                i += 1

        return result

