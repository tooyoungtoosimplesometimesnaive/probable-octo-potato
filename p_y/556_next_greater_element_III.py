class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))
        if len(n) <= 1:
            return -1

        i = len(n) - 1 - 1
        while i >= 0:
            if n[i] < n[i + 1]:
                break
            i -= 1
        if i < 0:
            return -1
        
        j = len(n) - 1
        while j > i:
            if n[j] > n[i]:
                n[j], n[i] = n[i], n[j]
                break
            j -= 1
        self.reverse_n(n, i + 1, len(n) - 1)
        result = int(''.join(n))
        return result if result <= 2**31 - 1 else -1

    def reverse_n(self, n, i, j):
        while i < j:
            n[i], n[j] = n[j], n[i]
            i += 1
            j -= 1

