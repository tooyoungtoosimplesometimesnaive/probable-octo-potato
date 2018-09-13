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
    result = 0
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        def get_depth(nl):
            d = 0
            #print('here')
            for k in nl:
                if not k.isInteger():
                    d = max(get_depth(k.getList()) + 1, d)
                else:
                    d = max(d, 1)
            return d

        depth = get_depth(nestedList)
        #print(depth)
        
        def calc(nl, level):
            for k in nl:
                if k.isInteger():
                    self.result += (k.getInteger() * (depth - level))
                else:
                    calc(k.getList(), level + 1)
            
        #for i in nestedList:
        calc(nestedList, 0)
        return self.result
            
