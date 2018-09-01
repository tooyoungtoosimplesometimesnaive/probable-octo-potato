class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = collections.defaultdict(list)
        for k, v in zip(s, range(0, len(s))):
            m[k].append(v)
        for c in s:
            if len(m[c]) == 1:
                return m[c][0]
        return -1
            

