class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        match = [-1] * len(S)
        
        for i in range(len(sources)):
            if S[indexes[i]:].startswith(sources[i]):
                match[indexes[i]] = i
        i = 0
        result = []
        while i < len(S):
            if match[i] >= 0:
                for c in targets[match[i]]:
                    result.append(c)
                i += len(sources[match[i]])
            else:
                result.append(S[i])
                i += 1
        
        
                
        return "".join(result)

