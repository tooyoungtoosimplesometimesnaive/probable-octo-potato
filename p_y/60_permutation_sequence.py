class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        l = [i for i in range(1, n + 1)]
        # the fractorial list for easy use. f[k] = k!
        f = [1 for i in range(n + 1)]
        i = 1
        while i < len(f):
            f[i] = i * f[i - 1]
            i += 1

        # self.get_perm(l, 1)
        k -= 1
        result = ''
        i = 1
        while i <= n:
            index = k // f[n - i]
            result += str(l[index])
            l.pop(index)
            k = k - index * f[n - i]
            i += 1

        return result
            
