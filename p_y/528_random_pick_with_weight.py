class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.size = sum(w)
        self.a_weights = [w[0]]
        for k in w[1:]:
            self.a_weights.append(self.a_weights[-1] + k)
        print(self.a_weights)

    def pickIndex(self):
        """
        :rtype: int
        """
        r = random.randrange(self.size) + 1
        i, j = 0, len(self.a_weights) - 1
        while i < j:
            mid = (i + j) // 2
            if self.a_weights[mid] == r:
                return mid
            elif self.a_weights[mid] < r:
                i = mid + 1
            else:
                j = mid
        return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
