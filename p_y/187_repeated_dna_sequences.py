class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = collections.defaultdict(int)
        for i in range(len(s) - 9):
            #print(i)
            dna = s[i:i + 10]
            m[dna] += 1
        result = []
        for k,v in m.items():
            if v >= 2:
                result.append(k)
        
        return result
            
