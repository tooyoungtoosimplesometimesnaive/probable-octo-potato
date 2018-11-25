class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        if l == 0: return 0

        left = [1] * l
        right = [1] * l
        
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        
        result = 0
        for left_candy, right_candy in zip(left, right):
            result += max(left_candy, right_candy)
        return result

