class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda p: p[0])
        
        chain = [1] * len(pairs)
        result = 0
        for i in range(len(pairs)):
            for k in range(i):
                if pairs[k][1] < pairs[i][0]:
                    chain[i] = max(chain[i], chain[k] + 1)
            result = max(result, chain[i])
        return result

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda p: p[0])

        chain = [1] * len(pairs)
        result = 0
        for i in range(len(pairs)):
            for k in range(i - 1, -1, -1):
                if pairs[k][1] < pairs[i][0]:
                    chain[i] = max(chain[i], chain[k] + 1)
                    break
            result = max(result, chain[i])
        return result
# Other solution: Greedy
class Solution(object):
    def findLongestChain(self, pairs):
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans

