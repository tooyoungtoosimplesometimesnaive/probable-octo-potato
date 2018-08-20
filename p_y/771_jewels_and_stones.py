class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        """
        s = set(J)
        count = 0
        for stone in S:
            if stone in s:
                count += 1
        return count
        """
        
        return sum([S.count(j) for j in J])
    
