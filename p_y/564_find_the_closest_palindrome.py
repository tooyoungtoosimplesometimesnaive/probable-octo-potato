class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        def mirror(n): # returns a string
            n = str(n)
            if len(n) % 2 == 0:
                return n[:len(n) // 2] + n[:len(n)//2][::-1]
            else:
                return n[:len(n) // 2 + 1] + n[:len(n)//2][::-1]
        
        order = 10 ** (len(n) // 2)
        #print(mirror(int(n)))
        # Do the mirror directly.
        no_change = int(mirror(int(n)))
        larger = int(mirror(int(n) // order * order + order))
        smaller = int(mirror(int(n) // order * order - 1))
        #print(no_change, larger, smaller)
        if no_change > int(n):
            larger = min(larger, no_change)
        elif no_change < int(n):
            smaller = max(smaller, no_change)
        
        result = smaller if int(n) - smaller <= larger - int(n) else larger
        return str(result)

