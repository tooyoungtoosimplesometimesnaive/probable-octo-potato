class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        m = collections.Counter()
        for a in A:
            for b in B:
                m[a + b] += 1
        
        result = 0
        for c in C:
            for d in D:
                result += m[-c-d]
        return result
        
