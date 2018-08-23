class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        B_dict = dict(zip(B, list(range(len(B)))))
        return list(map(lambda a: B_dict[a], A))


