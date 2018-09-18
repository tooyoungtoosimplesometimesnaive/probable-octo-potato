class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False

        def check(d):
            for k, v in d.items():
                if v != 0:
                    return False
            return True

        d = collections.defaultdict(int)
        tot = len(s1)
        for i in s1:
            d[i] += 1
        
        for k in range(len(s1)):
            if s2[k] in d:
                d[s2[k]] -= 1

        if check(d):
            return True
        i, j = 0, len(s1)
        
        while j < len(s2):

            if s2[j] in d:
                d[s2[j]] -= 1

            if s2[i] in d:
                d[s2[i]] += 1

            j += 1
            i += 1

            if check(d):
                return True

        return False
