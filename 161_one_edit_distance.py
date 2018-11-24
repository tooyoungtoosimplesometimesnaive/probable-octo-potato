class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        if abs(len(s) - len(t)) >= 2:
            return False
        if len(s) == len(t):
            diff_count = 0
            for a, b in zip(s, t):
                if a != b:
                    diff_count += 1
                if diff_count > 1:
                    return False
        else:
            diff_count = 0
            i, j = 0, 0
            # s is the bigger:
            s, t = (s, t) if len(s) > len(t) else (t, s)
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
                    i += 1
                else:
                    i += 1
                    j += 1
        return True

