class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1
        skip_s = 0
        skip_t = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    i -= 1
                    skip_s += 1
                elif skip_s > 0:
                    i -= 1
                    skip_s -= 1
                else:
                    break
            
            while j >= 0:
                if T[j] == '#':
                    j -= 1
                    skip_t += 1
                elif skip_t > 0:
                    j -= 1
                    skip_t -= 1
                else:
                    break
            
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            
            if (i >= 0) != (j >= 0):
                return False
            
            i -= 1
            j -= 1
        return True

