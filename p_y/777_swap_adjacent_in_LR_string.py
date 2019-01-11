class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        
        
        i = 0
        j = 0
        
        while i < len(start) and j < len(end):
        
            while i < len(start) and start[i] == 'X':
                i += 1
            while j < len(end) and end[j] == 'X':
                j += 1

            # if one of the index is out of bound, then return False
            if (i < len(start) and j == len(end)) or (i == len(start) and j < len(end)):
                return False

            if i < len(start) and j < len(end):
                if start[i] != end[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                    return False

            i += 1
            j += 1
            
        return True
    
